# Generated by Django 5.1 on 2024-08-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('name', models.CharField(default='Default Name', max_length=100)),
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_number', models.CharField(max_length=20)),
                ('teacher_allocated', models.CharField(max_length=20)),
                ('course_start_time', models.TimeField()),
                ('course_end_time', models.TimeField()),
                ('course_day_of_week', models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], max_length=3)),
                ('seating_arrangement', models.JSONField(default=dict)),
                ('equipment', models.JSONField(default=list)),
            ],
        ),
    ]
