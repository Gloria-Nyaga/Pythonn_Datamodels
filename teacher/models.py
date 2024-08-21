from django.db import models
from classroom.models import Classroom

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=20)
    teacher_id = models.PositiveIntegerField()
    teacher_course = models.CharField(max_length=20)
    teacher_occupation = models.CharField(max_length=20)
    salary = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    teacher_headshot = models.ImageField(blank=True, null=True)
    assigned_classrooms = models.ManyToManyField(Classroom, related_name='teachers_assigned')

    # objects = models.Manager()

    # class Meta:
    # ordering = ['first_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
