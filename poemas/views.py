# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Q
from django.views.generic import ListView

from poemas.forms import PoemaForm
from poemas.models import Poema
from poemas.settings import PUBLIC

class PoemasQuerySet(object):

    def get_poemas_queryset(self, request):
        if not request.user.is_authenticated(): #Si no está autenticado
            poemas = Poema.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser: #Sí es administrador
            poemas = Poema.objects.all()
        else: #Si está autenticado
            poemas = Poema.objects.filter(Q(owner=request.user) | Q(visibility=PUBLIC))
        return poemas

class HomeView(View, PoemasQuerySet):
    def get(self, request):
        """
        Está función devuelve el home de mi página
        :param request:
        :return:
        """
        #poemas = Poema.objects.filter(visibility=PUBLIC).order_by('-created_at')
        poemas = self.get_poemas_queryset(request).order_by('-created_at')
        context = {
            "poemas_list" : poemas[:]
        }

        return render(request, 'poemas/home.html',context)

class DetailView(View, PoemasQuerySet):
    def get(self, request, pk):
        """
        Carga el detalle de un poema
        :param request: HttpRequest
        :param pk: id del poema
        :return: HttpResponse
        """
        possible_poema = self.get_poemas_queryset(request).filter(pk=pk).select_related('owner')
        poema = possible_poema[0] if len(possible_poema) >= 1 else None
        if poema is not None:
            context = {
                "poema": poema
            }
            return render(request, 'poemas/detail.html', context)
        else:
            return HttpResponseNotFound("No existe el poema o no tienes el acceso permitido")

class CreateView(View):
    @method_decorator(login_required())
    def get(self, request):
        """
       Método para crear un nuevo poema
       :param request:
       :return:
       """
        form = PoemaForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'poemas/new_poema.html', context)

    @method_decorator(login_required())
    def post(self, request):
        success_message = ''
        poema_with_owner = Poema()
        poema_with_owner.owner = request.user  # Asigno el user al owner

        form = PoemaForm(request.POST, instance=poema_with_owner)

        if form.is_valid():
            new_poema = form.save()  # Guarda el objeto y lo devuelve
            form = PoemaForm()
            success_message = 'Guardado con exito'
            success_message += '<a href="{0}">'.format(reverse('poemas_detail', args={new_poema.pk}))
            success_message += 'Ver Poema'
            success_message += '</a>'
        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'poemas/new_poema.html', context)

class PoemaListView(View, PoemasQuerySet):
    def get(self, request):
        """
        Devuelve:
        Las fotos públicas si el usuario no está autenticado
        Las fotos del usuario auténticado y las públicas de otros
        Todas las fotos si es superadministrador
        :param request:
        :return:
        """
        poemas = self.get_poemas_queryset(request)

        context = {
            'poemas': poemas,
        }
        return render(request, 'poemas/poemas_list.html', context)

class UserPoemasView(ListView):
    model = Poema
    template_name = 'poemas/user_poemas.html'

    def get_queryset(self):
        queryset = super(UserPoemasView, self).get_queryset()
        return queryset.filter(owner=self.request.user)
