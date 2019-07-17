from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'name', 'get_short_name', 'email', 'password']
