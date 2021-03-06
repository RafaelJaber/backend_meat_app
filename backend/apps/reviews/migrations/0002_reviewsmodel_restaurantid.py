# Generated by Django 2.2.3 on 2019-07-11 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20190711_1241'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewsmodel',
            name='restaurantId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.RestaurantModel', verbose_name='Restaurant'),
            preserve_default=False,
        ),
    ]
