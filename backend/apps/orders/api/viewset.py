from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import Order
from backend.apps.orders_items.models import OrderItem
from backend.apps.menu.models import MenuModel
from .serializers import OrderSerializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
User = get_user_model()


class OrderViewSet(ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    def create(self, request, *args, **kwargs):
        request_data = request.data

        key = request.headers._store['authorization'][1].split()[1]
        token = Token.objects.get(key__exact=key)
        item_order = Order.objects.create(
            user=token.user,
            name=request_data['name'],
            email=request_data['email'],
            address=request_data['address'],
            number=request_data['number'],
            complement=request_data['complement'],
            paymentOption=request_data['paymentOption']
        )
        add_item = get_object_or_404(Order, pk=item_order.id)

        for item in request_data['orderItems']:
            menu = get_object_or_404(MenuModel, id=item['menuId'])
            item_create = OrderItem.objects.create(
                menu=menu,
                quantity=item['quantity']
            )
            add_item.orderItems.add(item_create)
        add_item.save()

        return Response({'response': item_order.id})
