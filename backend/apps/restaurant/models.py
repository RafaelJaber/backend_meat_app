from django.db import models


class RestaurantModel(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    slug = models.SlugField(verbose_name='Slug')
    deliveryEstimate = models.CharField(verbose_name='Tempo de Entrega', max_length=50)
    imagePath = models.ImageField(upload_to='restaurant', verbose_name='Logo')
    category = models.CharField(verbose_name='Categoria', max_length=100)
    rating = models.DecimalField(verbose_name='Avaliação', blank=True, null=True, decimal_places=2, max_digits=3)
    about = models.TextField(verbose_name='Sobre')
    hours = models.CharField(verbose_name='Horas de Funcionamento', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'
        ordering = ['name']
