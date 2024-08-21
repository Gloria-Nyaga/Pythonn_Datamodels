from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from course.models import Course
# from course.models import Course
from classPeriod.models import ClassPeriod
from classroom.models import Classroom
from datetime import datetime


# class StudentSerializer(serializers.ModelSerializer):
#     courses = CourseSerializer( many = True )
#     class Meta:
#         model = Student
#         fields = "__all__"
#         exclude = ["email"]

class minimalStudentSerializers(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Student
        fields=["full_name","email"]  



class minimalClassroomSerializer(serializers.ModelSerializer):
    check_name = serializers.SerializerMethodField()

    def get_check_name(self, object): 
        return f"{object.name}"  

    class Meta:
        model = Classroom
        fields = ["name", "check_name"]


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields= '__all__'



class minimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, object):
        return f"{object.teacher_name}"

    class Meta:
          model = Teacher
          fields = ["teacher_name", "teacher_salary", "full_name"]        


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = '__all__'

class minimalClassPeriodSerializer(serializers.ModelSerializer):
    period_name = serializers.SerializerMethodField()
    def get_period_name(self,object):
        return f"{object.name}"
    class Meta:
        model = ClassPeriod
        fields = ["name","class_period_classroom","period_name"]  


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'        


class StudentSerializers(serializers.ModelSerializer):
    classes= ClassroomSerializer(many=True)
    class Meta:
        model=Student
        fields='__all__'   


class ClassroomSerializers(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        fields='__all__'  