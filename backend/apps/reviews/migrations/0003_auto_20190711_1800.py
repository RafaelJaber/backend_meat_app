# Generated by Django 2.2.3 on 2019-07-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_reviewsmodel_restaurantid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewsmodel',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Avaliação'),
        ),
    ]
