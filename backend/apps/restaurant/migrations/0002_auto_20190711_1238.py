# Generated by Django 2.2.3 on 2019-07-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurantmodel',
            options={'ordering': ['name'], 'verbose_name': 'Restaurante', 'verbose_name_plural': 'Restaurantes'},
        ),
        migrations.AddField(
            model_name='restaurantmodel',
            name='category',
            field=models.CharField(default='', max_length=100, verbose_name='Categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurantmodel',
            name='rating',
            field=models.IntegerField(blank=True, null=True, verbose_name='Avaliação'),
        ),
        migrations.AddField(
            model_name='restaurantmodel',
            name='slug',
            field=models.SlugField(default='', verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
