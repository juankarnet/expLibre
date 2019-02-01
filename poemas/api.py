from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from poemas.models import Poema
from poemas.serializers import PoemaSerializer, PoemaListSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# class PoemaListAPI(APIView):
#     def get(self, request):
#         poemas = Poema.objects.all()
#         serializer = PoemaSerializer(poemas, many=True)
#         return Response(serializer.data)
from poemas.views import PoemasQuerySet

class PoemaAPIGeneral(PoemasQuerySet):
    queryset = Poema.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        return self.get_poemas_queryset(self.request)

class PoemaViewSet(PoemaAPIGeneral, ModelViewSet):

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('nombre', 'texto', 'owner__first_name')
    ordering_fields = ('nombre', 'owner')

    def get_serializer_class(self):
        if self.action == 'list':
            return PoemaListSerializer
        else:
            return PoemaSerializer


class PoemaListAPI(PoemaAPIGeneral, ListCreateAPIView):

    def get_serializer_class(self):
       return PoemaSerializer if self.request.method == 'POST' else PoemaListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PoemaDetailAPI(PoemaAPIGeneral, RetrieveUpdateDestroyAPIView):
    serializer_class = PoemaSerializer