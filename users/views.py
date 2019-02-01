# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_user, authenticate, login as login_user
from django.views import View

from users.forms import LoginForm

class LoginView(View):

    def get(self, request):

        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):

        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('usr')
            user_pwd = form.cleaned_data.get('pwd')
            user = authenticate(username=user_name, password=user_pwd)
            if user is None:
                error_messages.append('Nombre de Usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    login_user(request, user)
                    url = request.GET.get('next', 'poemas_home')
                    return redirect(url)
                else:
                    error_messages.append("El usuario no está activo")
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout_user(request)
        return redirect('poemas_home')



# def login(request):
#
#     error_messages = []
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data.get('usr')
#             user_pwd =  form.cleaned_data.get('pwd')
#             user = authenticate(username=user_name, password = user_pwd)
#             if user is None:
#                 error_messages.append('Nombre de Usuario o contraseña incorrectos')
#             else:
#                 if user.is_active:
#                     login_user(request, user)
#                     url = request.GET.get('next','poemas_home')
#                     return redirect(url)
#                 else:
#                     error_messages.append("El usuario no está activo")
#     else:
#         form = LoginForm()
#     context = {
#         'errors': error_messages,
#         'login_form':form
#     }
#     return render(request, 'users/login.html', context)
#
# def logout(request):
#     if request.user.is_authenticated:
#         logout_user(request)
#     return redirect('poemas_home')
#
#
