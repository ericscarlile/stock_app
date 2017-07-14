from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView
import urllib.request
import json

from .models import Stocks

# Create your views here.

class APIView(TemplateView):

    def post(self, request):
        pass

    def get(self, request):
        if self.request.is_ajax:
            if request.GET.get('search_url'):
                return self.ajax_search_bar(request)

    def ajax_search_bar(self, request):
        # Receive search_url
        # Get response from search_url
        # If response errors, search DB for results instead
        # Strip out JSONP, store as JSON.
        # Filter out non-US results.
        # Compile filtered dict as JSON.
        # Return JSON to ajax request.

        # As a test, just return the search_url to ajax call as a JSON.
        search_url = request.GET.get('search_url')
        exceptions = {}

        try:
            response = urllib.request.urlopen(search_url).read().decode('utf8')
            #data_json = response.split("(")[1].split(")")[0]
            #obj = json.loads(data_json)
            obj = json.loads(response)
            #results = obj['ResultSet']['Result']

            # Pull out all the results from US exchanges
            results = []
            us_results = {}
            us_results['Result'] = []

            for result in obj['ResultSet']['Result']:
                results.append(result)
            for result in results:
                if any(exch in result['exchDisp'] for exch in (
                        'BZX', 'BYX', 'BOX',
                        'C2', 'CBOE', 'CHX',
                        'EDGA', 'EDGX',
                        'IEX', 'ISE', 'MIAX',
                        'NASDAQ', 'BX', 'PHLX',
                        'NSX', 'NYSE', 'NYSE ARCA', 'NYSE MKT'
                )):
                    us_results['Result'].append(result)

                    #   results = []
                    #   us_results = {}
                    #   us_results['Result'] = []
                    #   for result in obj['ResultSet']['Result']:
                    #       results.append(result)
                    #   for indx, result in enumerate(results):
                    #       if any():
                    #           us_results['Result'].append(result)
        except:
            pass

        try:
            response_dict = JsonResponse(us_results)
            return response_dict
        except:
            exceptions['JSONBuild'] = 'Error creating JSON response.'
            response_dict = JsonResponse(exceptions)
            return response_dict
