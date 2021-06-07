from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from lotteryapp.forms import CustomUserCreationForm, LoginUserForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'lotteryapp/authorization.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return super(SignUpView, self).get(request, *args, **kwargs)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'lotteryapp/profile.html'
    success_url = reverse_lazy('index')
