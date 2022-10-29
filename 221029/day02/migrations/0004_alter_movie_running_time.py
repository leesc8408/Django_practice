# Generated by Django 3.2.13 on 2022-10-29 12:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day02', '0003_alter_movie_running_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='running_time',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]