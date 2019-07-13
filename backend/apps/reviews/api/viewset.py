from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from ..models import ReviewsModel
from .serializers import ReviewsSerializers


class ReviewsViewSet(ModelViewSet):

    queryset = ReviewsModel.objects.all()
    serializer_class = ReviewsSerializers
    filter_backends = (filters.SearchFilter, )
    search_fields = ('restaurantId__slug', )
