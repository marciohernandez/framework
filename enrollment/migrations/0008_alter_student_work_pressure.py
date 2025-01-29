# Generated by Django 5.1.4 on 2025-01-29 21:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0007_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='work_pressure',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
