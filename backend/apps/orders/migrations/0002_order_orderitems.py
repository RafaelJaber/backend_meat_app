# Generated by Django 2.2.3 on 2019-07-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_items', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderItems',
            field=models.ManyToManyField(to='orders_items.OrderItem'),
        ),
    ]
