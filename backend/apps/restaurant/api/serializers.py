from rest_framework import serializers
from ..models import RestaurantModel


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantModel
        fields = (
            'id', 'name', 'rating', 'category', 'deliveryEstimate', 'imagePath', 'slug',
            'about', 'hours'
        )
