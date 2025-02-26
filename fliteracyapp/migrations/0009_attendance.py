# Generated by Django 4.0.4 on 2024-05-01 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fliteracyapp', '0008_fl_attendants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fliteracyapp.fl_event')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fliteracyapp.nssfmember')),
            ],
        ),
    ]
