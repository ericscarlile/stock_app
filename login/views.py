from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from stock_app.views import IndexView

class LoginView(TemplateView):
    template_name = 'login/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login/login.html', {
                'error_message': 'Failed login'
            })


class CreateUserView(TemplateView):
    #User = get_user_model()
    template_name = 'login/create.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        error_message = ''
        if request.POST['username']:
            username = request.POST['username']
        else:
            error_message += 'You must enter a username.\n'

        if request.POST['password']:
            password = request.POST['password']
        else:
            error_message += 'You must enter a password.\n'

        if request.POST['email']:
            email = request.POST['email']
        else:
            error_message += 'You must enter an email.\n'

        if not error_message:
            User = get_user_model()
            user = User.objects.create_user(username, email, password)
            user.save()

            login(request, user)
            return redirect('index')

        return render(request, 'login/create.html', {
            'error_message': error_message
        })


    def get_context_data(self, **kwargs):
        return None


class LogoutView(TemplateView):
    template_name = 'login/login.html'

    def get(self, request):
        logout(request)
        return redirect('login_view')
