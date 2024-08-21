from django.db import models

from classroom.models import Classroom
from teacher.models import Teacher

# Create your models here.


class ClassPeriod(models.Model):
    DAY_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    class_period_classroom = models.CharField(max_length=20)
    class_period_course_taught = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    class_period_Day_of_the_week = models.CharField(max_length=20)
    teacher = models.ManyToManyField(Teacher)

    objects = models.Manager()
   
    def __str__(self):
        return f"{self.class_period_course_taught} teaches {self.class_period_classroom}"

class ClassPeriodClassPeriod(models.Model):
    class_period = models.ForeignKey(ClassPeriod, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
