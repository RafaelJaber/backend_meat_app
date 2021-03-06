# Generated by Django 2.2.3 on 2019-07-11 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0003_auto_20190711_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagePath', models.ImageField(upload_to='menu', verbose_name='Imagem')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Preço R$')),
                ('restaurantId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.RestaurantModel', verbose_name='Restaurante')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
    ]
