# Generated by Django 5.0.3 on 2024-05-31 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_diary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
