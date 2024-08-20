from student.models import Student
from classroom.models import Classroom
from courses.models import Courses
from teacher.models import Teacher
from classperiods.models import Class_Period
from rest_framework import serializers


class minimalStudentSerializers(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Student
        fields=["full_name","email"]  



class minimalClassesSerializer(serializers.ModelSerializer):
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


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class Class_PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Period
        fields = '__all__'

class minimalClass_PeriodSerializer(serializers.ModelSerializer):
    period_name = serializers.SerializerMethodField()
    def get_period_name(self,object):
        return f"{object.name}"
    class Meta:
        model = Class_Period
        fields = ["name","class_period_classroom","period_name"]          


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'        


class StudentSerializers(serializers.ModelSerializer):
    classes= ClassesSerializer(many=True)
    class Meta:
        model=Student
        fields='__all__'   