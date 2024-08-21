
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial')
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('course_department', models.CharField(max_length=20)),
                ('course_start_date', models.DateField()),
                ('course_end_date', models.DateField()),
                ('course_code', models.PositiveSmallIntegerField()),
                ('course_level', models.CharField(max_length=20)),
                ('maximum_attendees', models.PositiveSmallIntegerField()),
                ('course_exams', models.CharField(max_length=20)),
                ('course_fee', models.PositiveSmallIntegerField()),
                ('teacher', models.ForeignKey(on_delete=models.CASCADE, related_name='taught_courses', to='teacher.Teacher')),
                ('students', models.ManyToManyField(to='student.Student')),
            ],
        ),
    ]
