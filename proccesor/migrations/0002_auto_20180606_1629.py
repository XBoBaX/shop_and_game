# Generated by Django 2.0.6 on 2018-06-06 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proccesor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'Цена на процессоры', 'verbose_name_plural': 'цена на процессоры'},
        ),
        migrations.AlterField(
            model_name='price',
            name='tovar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tovar_id', to='proccesor.Proc'),
        ),
    ]
