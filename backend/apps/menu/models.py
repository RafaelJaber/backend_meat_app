from django.db import models
from backend.apps.restaurant.models import RestaurantModel


class MenuModel(models.Model):
    imagePath = models.ImageField(upload_to='menu', verbose_name='Imagem')
    name = models.CharField(verbose_name='Nome', max_length=50)
    description = models.TextField(verbose_name='Descrição')
    price = models.DecimalField(verbose_name='Preço R$', decimal_places=2, max_digits=4)
    restaurantId = models.ForeignKey(RestaurantModel, verbose_name='Restaurante', on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurantId.name + ' - ' + self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

