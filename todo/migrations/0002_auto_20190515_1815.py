# Generated by Django 2.2.1 on 2019-05-15 18:15

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='list',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(1, '낮음'), (2, '보통'), (3, '높음')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
    ]
