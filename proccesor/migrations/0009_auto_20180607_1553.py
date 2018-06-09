# Generated by Django 2.0.6 on 2018-06-07 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proccesor', '0008_auto_20180607_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='adress1',
            field=models.TextField(blank=True, null=True, verbose_name='ссылка на 1ый магазин'),
        ),
        migrations.AlterField(
            model_name='price',
            name='adress10',
            field=models.TextField(blank=True, null=True, verbose_name='ссылка на 10ый магазин'),
        ),
        migrations.AlterField(
            model_name='price',
            name='adress2',
            field=models.TextField(blank=True, null=True, verbose_name='ссылка на 2ый магазин'),
        ),
        migrations.AlterField(
            model_name='price',
            name='adress3',
            field=models.TextField(blank=True, null=True, verbose_name='ссылка на 3ый магазин'),
        ),
        migrations.AlterField(
            model_name='price',
            name='adress4',
            field=models.TextField(blank=True, null=True, verbose_name='ссылка на 4ый магазин'),
        ),
        migrations.AlterField(
            model_name='price',
            name='adress5',
            field=models.TextField(blank=True, null=True, verbose_name='ссылка на 5ый магазин'),
        ),
        migrations.AlterField(
            model_name='price',
            name='adress6',
            field=models.TextField(blank=True, null=True, verbose_name='ссылка на 6ый магазин'),
        ),
        migrations.AlterField(
            model_name='price',
            name='adress7',
            field=models.TextField(blank=True, null=True, verbose_name='ссылка на 7ый магазин'),
        ),
        migrations.AlterField(
            model_name='price',
            name='adress8',
            field=models.TextField(blank=True, null=True, verbose_name='ссылка на 8ый магазин'),
        ),
        migrations.AlterField(
            model_name='price',
            name='adress9',
            field=models.TextField(blank=True, null=True, verbose_name='ссылка на 9ый магазин'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена 1го магазина'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price10',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена 10го магазина'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена 2го магазина'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price3',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена 3го магазина'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price4',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена 4го магазина'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price5',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена 5го магазина'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price6',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена 6го магазина'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price7',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена 7го магазина'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price8',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена 8го магазина'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price9',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена 9го магазина'),
        ),
    ]
