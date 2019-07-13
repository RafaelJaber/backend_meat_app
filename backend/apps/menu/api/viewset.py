from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from ..models import MenuModel
from .serializer import MenuSerializer


class MenuViewSet(ModelViewSet):

    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('restaurantId__slug',)
