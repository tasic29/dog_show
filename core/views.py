from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from .models import MyUser
from . forms import CreateUserForm, LoginForm


def thank_you(request):
    if request.method == 'POST':
        return HttpResponse("Thank you for your submission!")

    return render(request, 'core/thank_you.html')


class UsersListView(ListView):
    model = MyUser
    context_object_name = 'users'
    template_name = 'core/myuser_list.html'


class CreateNewUser(CreateView):
    form_class = CreateUserForm
    template_name = 'core/create_user.html'
    success_url = reverse_lazy('core:login')


class MyLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'core/login.html'


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('core:users-list')
