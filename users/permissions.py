# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado tiene permiso para
        realizar las acciones GET, POST, PUT or DELETE
        :param request:
        :param view:
        :return:
        """
        #Para crear un usuario cualquiera puede
        # from users.api import UserDetailAPI
        # if request.method == 'POST':
        if view.action == 'create':
            return True
        #El superusuario puede hacer cualquier cosa
        elif request.user.is_superuser:
            return True
        # elif isinstance(view, UserDetailAPI):
        elif view.action in ['retrieve', 'update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado tiene permiso para
        realizar la acción GET, PUT or DELETE
        sobre el objeto indicado
        :param request:
        :param view:
        :param obj:
        :return:
        """
        return request.user.is_superuser or request.user == obj
