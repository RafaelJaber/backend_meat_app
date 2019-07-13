from django.db import models
from backend.apps.restaurant.models import RestaurantModel


class ReviewsModel(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=150)
    date = models.DateTimeField(verbose_name='Data', auto_now_add=True)
    rating = models.DecimalField(verbose_name='Avaliação', decimal_places=1, max_digits=2)
    comments = models.TextField(verbose_name='Comentário', blank=True, null=True)
    restaurantId = models.ForeignKey(RestaurantModel, verbose_name='Restaurant', on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurantId.name + ' - ' + self.name

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
