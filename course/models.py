from django.db import models

from student.models import Student

class Course(models.Model):
    course_name= models.CharField(max_length=20)
    course_department = models.CharField(max_length=20)
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    course_code = models.PositiveSmallIntegerField()
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE, related_name='taught_courses')
    course_level = models.CharField(max_length=20)
    maximum_attendees = models.PositiveSmallIntegerField()
    course_exams = models.CharField(max_length=20)
    course_fee = models.PositiveSmallIntegerField()
    students = models.ManyToManyField(Student)


    def __str__(self) -> str:
        return f"({self.course_code}) {self.course_name}"
