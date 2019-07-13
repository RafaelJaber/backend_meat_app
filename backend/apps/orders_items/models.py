from django.db import models
from backend.apps.menu.models import MenuModel


class OrderItem(models.Model):
    menu = models.ForeignKey(MenuModel, verbose_name='Item', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Quantidade')

    def __str__(self):
        return str(self.quantity) + 'x' + self.menu.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

