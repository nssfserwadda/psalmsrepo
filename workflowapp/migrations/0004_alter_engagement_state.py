# Generated by Django 4.0.4 on 2023-07-15 11:28

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('workflowapp', '0003_engagement_reviewer_engagement_state_engagementlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagement',
            name='state',
            field=django_fsm.FSMField(choices=[('recorded', 'Recorded'), ('forwarded', 'Forwarded'), ('cancelled', 'Cancelled'), ('rejected', 'Rejected'), ('approved', 'Approved')], default='recorded', max_length=50),
        ),
    ]
