from rest_framework import serializers
from ..models import ReviewsModel


class ReviewsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ReviewsModel
        fields = 'name', 'date', 'rating', 'comments'
