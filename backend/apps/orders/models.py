from django.db import models
from backend.apps.orders_items.models import OrderItem


class Order(models.Model):
    MONEY = 'MON'
    CART_DEB = 'DEB'
    CART_MEAL = 'REF'

    PAYMENTS = (
        (MONEY, 'Dinheiro'),
        (CART_DEB, 'Cartão de Débito'),
        (CART_MEAL, 'Cartão Refeição'),
    )

    name = models.CharField(verbose_name='Nome', max_length=150)
    email = models.CharField(verbose_name='Email', max_length=100)
    address = models.CharField(verbose_name='Endereço', max_length=100)
    number = models.IntegerField(verbose_name='Número')
    complement = models.CharField(verbose_name='Complemento', max_length=100, blank=True, null=True)
    paymentOption = models.CharField(verbose_name='Pagamento', max_length=4, choices=PAYMENTS)
    orderItems = models.ManyToManyField(OrderItem, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
