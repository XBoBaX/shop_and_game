# Generated by Django 2.0.6 on 2018-06-07 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motherboard', '0004_motherboard_min_price_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Кол-во магазинов'),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='min_price_ad',
            field=models.TextField(blank=True, null=True, verbose_name='мин адрес'),
        ),
    ]
