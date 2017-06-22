from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'stock_app/index.html'

    def get_queryset(self):
        return None
