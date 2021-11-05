# Generated by Django 3.2.9 on 2021-11-05 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=200)),
                ('ingrediantes', models.TextField()),
                ('modo_de_preparo', models.TextField()),
                ('tempo_preparo', models.IntegerField()),
                ('rendimento', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=200)),
                ('data_receita', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
