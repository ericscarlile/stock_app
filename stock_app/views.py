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
from django.core.exceptions import ObjectDoesNotExist
from yahoo_finance import Share
from django.utils import timezone

from .models import Stock, User


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'stock_app/index.html'
    test_list = []



    def get(self, request):
        self.test_list = []
        self.update_stocks(request)
        return render(request, self.template_name, {
            'test_info': self.test_list,
        })

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            return self.ajax(request)

    def update_stocks(self, request):
        user = User.objects.get(username=request.user)
        for stock in list(user.stocks.all()):
            self.test_list.append(stock.ticker)


class StockDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'stock_app/stock_detail.html'
    model = Stock

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            return self.ajax(request)

        return render(request, self.template_name, {
            #'stock_tracked': self.stock_tracked(request, symbol)
        })

    def get(self, request, symbol):

        try:
            stock = Stock.objects.get(ticker=symbol)
        except ObjectDoesNotExist:
            stock_info = Share(symbol)
            stock = Stock(
                name=stock_info.get_name(),
                ticker=symbol,
                price=stock_info.get_price(),
                price_target=stock_info.get_one_yr_target_price(),
                is_bullish=None,
                last_updated=timezone.now()
            )
            stock.save()

            try:
                stock = Stock.objects.get(ticker=symbol)
            except ObjectDoesNotExist:
                stock = "Still can not pull stock."

        return render(request, self.template_name, {
            'stock': stock,
            'stock_tracked': self.stock_tracked(request, symbol)
        })

    def ajax(self, request):

        user = User.objects.get(username=request.user);
        action = request.POST.get('action', '');
        symbol = request.POST.get('symbol', '');

        response_dict = {
            'success': 'initial',
        }
        if action == 'add_stock':
            try:
                user.stocks.add(Stock.objects.get(ticker=symbol))
                user.save()
                response_dict = {
                    'success': 'try',
                }
            except:
                response_dict = {
                    'success': 'exception add_stock',
                }

        if action == 'remove_stock':
            try:
                user.stocks.remove(Stock.objects.get(ticker=symbol))
            except:
                response_dict = {
                    'success': 'exception remove_stock',
                }

        return HttpResponse(json.dumps(response_dict))

    def stock_tracked(self, request, symbol):
        user = User.objects.get(username=request.user);
        try:
            if user.stocks.get(ticker=symbol):
                return True
        except:
            return False


# This class has been replaced by ajax calls.
# It is still here in case a need for it is found in the near future.
# Will be removed after completion of the app if there is no need for it.
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
