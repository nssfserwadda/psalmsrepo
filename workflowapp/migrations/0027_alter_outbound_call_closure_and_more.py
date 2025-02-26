# Generated by Django 4.0.4 on 2024-03-06 10:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflowapp', '0026_outbound_call_closure_outbound_emotional_connection_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outbound',
            name='call_closure',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='outbound',
            name='emotional_connection',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25)]),
        ),
        migrations.AlterField(
            model_name='outbound',
            name='greeting_and_enthusiasm',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='outbound',
            name='hold_procedure',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='outbound',
            name='resolution_and_professionalism',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(35)]),
        ),
    ]
