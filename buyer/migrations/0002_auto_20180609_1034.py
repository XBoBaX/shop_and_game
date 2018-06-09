# Generated by Django 2.0.6 on 2018-06-09 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proccesor', '0012_price_count'),
        ('videokarta', '0006_auto_20180608_0309'),
        ('motherboard', '0005_auto_20180608_0218'),
        ('OP', '0004_auto_20180608_0218'),
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyed',
            name='mother',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='mother', to='motherboard.Motherboard'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyed',
            name='operative',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='ram', to='OP.Operative'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyed',
            name='proc',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='proc', to='proccesor.Proc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyed',
            name='video',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vid', to='videokarta.Videocard'),
            preserve_default=False,
        ),
    ]
