# Generated by Django 3.2.4 on 2021-07-15 10:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0026_auto_20210715_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='course_name',
            field=models.CharField(choices=[('0', 'Select'), ('BT101', 'BT101'), ('BT201', 'BT201'), ('BT202', 'BT202'), ('BT203', 'BT203'), ('BT204', 'BT204'), ('BT205', 'BT205'), ('BT206', 'BT206'), ('BT207', 'BT207'), ('BT208', 'BT208'), ('BT209', 'BT209'), ('BT211', 'BT211'), ('BT301', 'BT301'), ('BT302', 'BT302'), ('BT303', 'BT303'), ('BT304', 'BT304'), ('BT305', 'BT305'), ('BT306', 'BT306'), ('BT307', 'BT307'), ('BT308', 'BT308'), ('BT311', 'BT311'), ('BT312', 'BT312'), ('BT3xx', 'BT3xx'), ('BT401', 'BT401'), ('BT402', 'BT402'), ('BT4xx', 'BT4xx'), ('CL101', 'CL101'), ('CL201', 'CL201'), ('CL202', 'CL202'), ('CL203', 'CL203'), ('CL204', 'CL204'), ('CL205', 'CL205'), ('CL206', 'CL206'), ('CL207', 'CL207'), ('CL208', 'CL208'), ('CL209', 'CL209'), ('CL210H', 'CL210H'), ('CL211H', 'CL211H'), ('CL301', 'CL301'), ('CL302', 'CL302'), ('CL303', 'CL303'), ('CL304', 'CL304'), ('CL305', 'CL305'), ('CL306', 'CL306'), ('CL310', 'CL310'), ('CL311', 'CL311'), ('CL312', 'CL312'), ('CL313', 'CL313'), ('CL314H', 'CL314H'), ('CL315H', 'CL315H'), ('CL3xx', 'CL3xx'), ('CLxxx', 'CLxxx'), ('CL4xx', 'CL4xx')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 10, 51, 57, 440542, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 10, 51, 57, 495398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 10, 51, 57, 495398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 10, 51, 57, 495398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 10, 51, 57, 495398, tzinfo=utc)),
        ),
    ]
