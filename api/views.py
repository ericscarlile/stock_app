from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class APIView(TemplateView):

    def post(self, request):
        pass