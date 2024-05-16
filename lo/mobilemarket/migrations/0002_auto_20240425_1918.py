# Generated by Django 3.2.25 on 2024-04-25 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobilemarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmodel',
            name='maker',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, to='mobilemarket.maker'),
        ),
        migrations.AlterField(
            model_name='pmodel',
            name='url',
            field=models.URLField(default='http://mis.com'),
        ),
        migrations.AlterField(
            model_name='pphoto',
            name='url',
            field=models.URLField(default='http://mis.com'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pmodel',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.SET_DEFAULT, to='mobilemarket.pmodel', verbose_name='型號'),
        ),
    ]