# Generated by Django 2.0.6 on 2018-06-06 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motherboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motherboard',
            name='interf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mother2', to='videokarta.Connection'),
        ),
    ]
