# Generated by Django 3.2.9 on 2021-12-09 10:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(choices=[('0', 'Select'), ('SWC', 'SWC'), ('CODING CLUB', 'CODING CLUB'), ('AERO CLUB', 'AERO CLUB'), ('ASTRO CLUB', 'ASTRO CLUB'), ('CA CLUB', 'CA CLUB'), ('EE CLUB', 'EE CLUB'), ('PRAKRITI CLUB', 'PRAKRITI CLUB'), ('FNC CLUB', 'FNC CLUB'), ('ROBOTICS CLUB', 'ROBOTICS CLUB'), ('ED CLUB', 'ED CLUB'), ('UG CLUB', 'UG CLUB'), ('ALCHER CLUB', 'ALCHER CLUB'), ('TECHNICHE CLUB', 'TECHNICHE CLUB'), ('SAIL CLUB', 'SAIL CLUB'), ('AI CLUB', 'AI CLUB'), ('CCD CLUB', 'CCD CLUB'), ('OTHER CLUB', 'OTHER CLUB')], max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('date', models.DateField(default=datetime.datetime(2021, 12, 9, 10, 59, 1, 489287, tzinfo=utc))),
                ('deadline', models.DateField(blank=True, default=datetime.datetime(2021, 12, 9, 10, 59, 1, 763496, tzinfo=utc), null=True)),
                ('time_from', models.TimeField(default=datetime.datetime(2021, 12, 9, 10, 59, 1, 763496, tzinfo=utc))),
                ('time_to', models.TimeField(default=datetime.datetime(2021, 12, 9, 10, 59, 1, 763496, tzinfo=utc))),
                ('remainder_date', models.DateField(default=datetime.datetime(2021, 12, 9, 10, 59, 1, 763496, tzinfo=utc))),
                ('remainder_time', models.TimeField(default=datetime.datetime(2021, 12, 9, 10, 59, 1, 764504, tzinfo=utc))),
                ('remainder', models.CharField(choices=[('0', 'Select'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Week before', 'Week before'), ('Custom', 'Custom')], default='None', max_length=12)),
                ('announcements', models.TextField(blank=True, default='', help_text='announcements should be seperated by comma, so that we can list them as points', null=True)),
                ('resources_upload', models.FileField(blank=True, null=True, upload_to='media/')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rsvp_users', models.ManyToManyField(related_name='rsvp_tasks', to='users.Profile')),
            ],
        ),
    ]
