# Generated by Django 4.0.4 on 2024-09-21 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback2024', '0014_whistleblowerlog_comment_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='whistleblowerlog',
            name='whistleblower',
            field=models.ForeignKey(default=12345, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='feedback2024.whistleblower'),
            preserve_default=False,
        ),
    ]
