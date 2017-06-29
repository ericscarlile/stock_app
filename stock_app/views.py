from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

import urllib.request
import json


class IndexView(LoginRequiredMixin, generic.ListView):

    def get(self, request):
        template_name = 'stock_app/index.html'
        return render(request, template_name)


class StockSearchView(LoginRequiredMixin, generic.ListView):

    def post(self, request, *args, **kwargs):
        if request.POST['search_key']:
            search_key = request.POST['search_key']
            search_url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback'.format(search_key)

            # The search_url will return a JSONP not a JSON.
            # This code formats the JSONP to a JSON so it can be used.
            response = urllib.request.urlopen(search_url).read().decode('utf8')
            data_json = response.split("(")[1].split(")")[0]
            obj = json.loads(data_json)

            return redirect(search_url)