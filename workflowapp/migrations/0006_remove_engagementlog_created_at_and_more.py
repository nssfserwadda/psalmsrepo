# Generated by Django 4.0.4 on 2023-07-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflowapp', '0005_alter_engagement_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engagementlog',
            name='created_at',
        ),
        migrations.AddField(
            model_name='engagementlog',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
