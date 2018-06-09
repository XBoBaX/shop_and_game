# Generated by Django 2.0.6 on 2018-06-09 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tovar_id', to='profiles.Profile')),
            ],
        ),
    ]
