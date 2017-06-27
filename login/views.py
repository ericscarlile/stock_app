from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login

from stock_app.views import IndexView


class LoginView(TemplateView):
    template_name = 'login/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # TODO: Uncomment login() when log in/out has been established.
            #login(request, user)

            return redirect('http://127.0.0.1:8000/')
        else:
            return render(request, 'login/login.html', {
                'error_message': 'Failed login'
            })

    def get_context_data(self, **kwargs):
        context = {}
        return context
