from django.shortcuts import render

from rest_framework.views import APIView
from student.models import Student
from classperiods.models import Class_Period
from classroom.models import Classroom
from teacher.models import Teacher
from courses.models import Courses
from rest_framework import status
from .serializers import StudentSerializers,minimalClass_PeriodSerializer, minimalClassesSerializer, minimalStudentSerializers, minimalTeacherSerializer
from .serializers import TeacherSerializer
from .serializers import ClassesSerializer
from .serializers import Class_PeriodSerializer
from .serializers import CoursesSerializer
from rest_framework.response import Response
from .serializers import minimalStudentSerializers

from dateutil import parser
from datetime import datetime, timedelta


class StudentListView(APIView):   
    def get(self, request):
        students = Student.objects.all()
        serializer = minimalStudentSerializers(students,many=True) 
        first_name = request.query_params.get("first_name")
        country = request.query_params.get("country")
        if first_name:
            students = students.filter(first_name = first_name)
        if country:
            students = students.filter(country = country)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class StudentDetailView(APIView):
    def get(self,request,id):
        student=Student.objects.get(id=id)
        serializer =StudentSerializers(student)
        return Response(serializer.data)   

    def put(self, request,id):
       student=Student.objects.get(id=id)
       serializer =StudentSerializers(student,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,id):
        student=Student.objects.get(id=id)
        serializer =StudentSerializers(student)
        student.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  

    def enroll_student(self,student,course_id):
        course = Courses.objects.get(id=course_id)
        student.courses.add(course)

    def unenroll_student(self,student,course_id):
        course = Courses.objects.get(id=course_id)
        student.courses.remove(course)    

    
    def add_to_class(self, student, class_id):
        class_obj = Classroom.objects.get(id=class_id)
        student.classes.add(class_obj)    

    def post(self,request,id):
        student = Student.objects.get(id=id)
        action = request.data.get("action") 

        if action == "enroll":
           course_id = request.data.get("course")
           self.enroll_student(student,course_id)
           return Response(status.HTTP_202_ACCEPTED)
        
        if action == "unenroll":
           course_id = request.data.get("course")
           self.unenroll_student(student,course_id)
           return Response(status.HTTP_202_ACCEPTED)
        
        elif action == "add_to_class":
            class_id = request.data.get("classes")
            self.add_to_class(student, class_id)
            return Response(status=status.HTTP_202_ACCEPTED)
        

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serialiizer = minimalTeacherSerializer(teachers,many=True)
        teacher_name = request.query_params.get("teacher name")
        teacher_salary = request.query_params.get("teacher salary")
        if teacher_name:
            teachers = teachers.filter(teacher_name == teacher_name)
        if teacher_salary:
            teachers = teachers.filter(teacher_salary == teacher_salary)
        return Response(serialiizer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
        

class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer =TeacherSerializer(teacher)
        return Response(serializer.data)   

    def put(self, request,id):
       teacher=Teacher.objects.get(id=id)
       serializer =TeacherSerializer(teacher,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer =TeacherSerializer(teacher)
        teacher.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  
    
    def assign_course(self, teacher, course_id):
        course = Courses.objects.get(id=course_id)
        teacher.courses.add(course)

    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")

        if action == "assign_course":
           course_id = request.data.get("course")
           self.assign_course(teacher,course_id)
           return Response(status.HTTP_202_ACCEPTED)

        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)  


class CoursesListView(APIView):
  def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)
  
  def post(self, request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class CoursesDetailView(APIView):
    def get(self,request,id):
        courses=Student.objects.get(id=id)
        serializer =CoursesSerializer(courses)
        return Response(serializer.data)   

    def put(self, request,id):
       courses=Courses.objects.get(id=id)
       serializer =CoursesSerializer(courses,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,id):
        courses=Courses.objects.get(id=id)
        serializer =CoursesSerializer(courses)
        courses.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)         
    

class ClassesListView(APIView):
  def get(self, request):
        classes = Classroom.objects.all()
        serializer = minimalClassesSerializer(classes,many=True)
        name= request.query_params.get("name")
        seating_arrangement = request.query_params.get("seating arrangement")
        if name:
            classes = classes.filter(name = name)
        if seating_arrangement:
            classes = classes.filter(seating_arrangement = seating_arrangement)
        return Response(serializer.data)
  
  def post(self, request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class ClassesDetailView(APIView):
    def get(self,request,id):
        classes=Classroom.objects.get(id=id)
        serializer =ClassesSerializer(classes)
        return Response(serializer.data)   

    def put(self, request,id):
       classe=Classroom.objects.get(class_id=id)
       serializer =ClassesSerializer(classe,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,id):
        classe=Classroom.objects.get(id=id)
        serializer =ClassesSerializer(classe)
        classe.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)      
    

class Classs_PeriodListView(APIView):
    def get(self, request):
        action = request.query_params.get('action')

        if action == 'weekly_timetable':
            return self.get_weekly_timetable(request)
        
        periods = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(periods, many=True)
        serializer = minimalClass_PeriodSerializer(periods,many=True)
        name= request.query_params.get("name")
        class_period_classroom = request.query_params.get("class period classroom")
        if name:
            periods = periods.filter(name == name)
        if class_period_classroom:
            periods = periods.filter(class_period_classroom == class_period_classroom)
        return Response(serializer.data)

    def get_weekly_timetable(self, request):
        start_date_str = request.query_params.get('start_date')
        if not start_date_str:
            start_date = datetime.now().date()
        else:
            try:
                start_date = parser.parse(start_date_str).date()
            except ValueError:
                return Response({"error": "Invalid date format. Please use YYYY-MM-DD."},
                                status=status.HTTP_400_BAD_REQUEST)

        end_date = start_date + timedelta(days=6)

        class_periods = Class_Period.objects.filter(
            date__range=[start_date, end_date]
        ).select_related('teacher', 'course', 'class_obj')

        timetable = {}
        for period in class_periods:
            day = period.date.strftime('%A')
            if day not in timetable:
                timetable[day] = []
            
            timetable[day].append({
                'time': period.time.strftime('%H:%M'),
                'course': period.course.name,
                'teacher': f"{period.teacher.first_name} {period.teacher.last_name}",
                'class': period.class_obj.name
            })

        return Response(timetable)

    def post(self, request):
        serializer = Class_PeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class Class_PeriodDetailView(APIView):
    def get(self,request,id):
        period=Class_Period.objects.get(id=id)
        serializer =Class_PeriodSerializer(Class_Period)
        return Response(serializer.data)   

    def put(self, request,id):
       period=Class_Period.objects.get(class_id=id)
       serializer =Class_PeriodSerializer(period,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,id):
        period=Class_Period.objects.get(id=id)
        serializer =Class_PeriodSerializer(period)
        period.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  
    
    def post(self, request):
        serializer = Class_PeriodSerializer(data=request.data)
        if serializer.is_valid():
            class_period = serializer.save()
            
            teacher_id = request.data.get("teacher_id")
            course_id = request.data.get("course_id")
            
            if teacher_id and course_id:
                teacher = Teacher.objects.get(id=teacher_id)
                course = Courses.objects.get(id=course_id)
                class_period.teacher = teacher
                class_period.course = course
                class_period.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

