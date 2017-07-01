from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
import html.parser

import urllib.request
import json


class IndexView(LoginRequiredMixin, generic.ListView):

    def get(self, request):
        template_name = 'stock_app/index.html'
        return render(request, template_name)

    def post(self, request):
        pass


class StockSearchView(LoginRequiredMixin, generic.ListView):

        def search_stock(self, request):
            template_name = 'stock_app/test.html'
            search_key = request.POST['search_key']
            search_url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback'.format(
                search_key)
            formatted_url = search_url.replace(" ", "%20")

            # The search_url will return a JSONP not a JSON.
            # This code formats the JSONP to a JSON so it can be used.
            response = urllib.request.urlopen(formatted_url).read().decode('utf8')
            data_json = response.split("(")[1].split(")")[0]
            obj = json.loads(data_json)
            results = obj['ResultSet']['Result']
            us_results = []
            for result in results:
                if any(exch in result['exchDisp'] for exch in (
                    'BZX', 'BYX', 'BOX',
                    'C2', 'CBOE', 'CHX',
                    'EDGA', 'EDGX',
                    'IEX', 'ISE', 'MIAX',
                    'NASDAQ', 'BX', 'PHLX',
                    'NSX', 'NYSE', 'NYSE ARCA', 'NYSE MKT'
                        )):
                    us_results.append(result['symbol'])

            return render(request, template_name, {
                'test_info': us_results
            })

        def post(self, request):
            if request.POST['search_key']:
                return self.search_stock(request)
