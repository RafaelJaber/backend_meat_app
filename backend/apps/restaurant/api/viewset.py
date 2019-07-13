from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from ..models import RestaurantModel
from .serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):

    serializer_class = RestaurantSerializer
    queryset = RestaurantModel.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'about', 'category')
    lookup_field = 'slug'


