from django.contrib import admin
from .models import Classroom
# Register your models here.

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_number', 'teacher_allocated', 'course_start_time', 'course_end_time', 'course_day_of_week')
    search_fields = ('name', 'room_number', 'teacher_allocated')
    list_filter = ('course_day_of_week',)
    ordering = ('name',)
    # If you want to enable editing of related students directly from Classroom admin:
    filter_horizontal = ('students',)