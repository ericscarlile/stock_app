from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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


class CreateUserView(TemplateView):
    template_name = 'login/create.html'

    def post(self, request, *args, **kwargs):
        error_message = ''
        if request.POST['username']:
            username = request.POST['username']
        else:
            error_message += 'You must enter a username.\n'

        if request.POST['password']:
            password = request.POST['password']
        else:
            info = 'no pass'
            error_message += 'You must enter a password.\n'

        if request.POST['email']:
            email = request.POST['email']
        else:
            error_message += 'You must enter an email.\n'

        if request.POST['first_name']:
            first_name = request.POST['first_name']
        else:
            error_message += 'You must enter a first name.\n'

        if request.POST['last_name']:
            last_name = request.POST['last_name']
        else:
            error_message += 'You must enter a last name.\n'

        if not error_message:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            return redirect('http://127.0.0.1:8000/')

        return render(request, 'login/create.html', {
            'error_message': error_message
        })

    def get_context_data(self, **kwargs):
        return None