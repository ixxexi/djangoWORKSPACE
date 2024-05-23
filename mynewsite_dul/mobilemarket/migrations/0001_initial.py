# Generated by Django 5.0.3 on 2024-04-19 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField(default='http://mis.com')),
                ('maker', models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, to='mobilemarket.maker')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='超值二手機', max_length=15)),
                ('description', models.TextField(default='暫無說明')),
                ('year', models.PositiveIntegerField(default=2016)),
                ('price', models.PositiveIntegerField(default=0)),
                ('pmodel', models.ForeignKey(default=4, on_delete=django.db.models.deletion.SET_DEFAULT, to='mobilemarket.pmodel', verbose_name='型號')),
            ],
        ),
        migrations.CreateModel(
            name='PPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='產品照片', max_length=20)),
                ('url', models.URLField(default='http://mis.com')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilemarket.product')),
            ],
        ),
    ]
