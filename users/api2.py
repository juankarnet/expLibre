from django.contrib.auth.models import User

from django.views.generic import View
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.pagination import PageNumberPagination

from django.shortcuts import get_object_or_404

from users.serializers import UserSerializer
from users.permissions import UserPermission


class UserListAPI(APIView, PageNumberPagination):

    permission_classes = (UserPermission,)

    def get(self, request):
        self.check_permissions(request)
        queryset = User.objects.all()
        users = self.paginate_queryset(queryset, request)
        serializer = UserSerializer(users, many=True)
        serialized_users = serializer.data
        return self.get_paginated_response(serialized_users)
        #return Response(serialized_users)

    def post(self, request):
        self.check_permissions(request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):

    permission_classes = (UserPermission,)

    def get(self, request, pk):
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)