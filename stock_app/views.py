from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class IndexView(LoginRequiredMixin, generic.ListView):

    def get(self, request):
        template_name = 'stock_app/index.html'
        return render(request, template_name)

