from django.urls import path
from .views import StudentListView, TeacherListView, CoursesListView, ClassesListView, Classs_PeriodListView,StudentDetailView,Class_PeriodDetailView,TeacherDetailView,CoursesDetailView,ClassesDetailView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list_view'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list_view'),
    path('classes/', ClassesListView.as_view(), name='classes_list_view'),
    path('courses/', CoursesListView.as_view(), name='courses_list_view'),
    path('periods/', Classs_PeriodListView.as_view(), name='class_period_list_view'),
    path('students/<int:id>/',StudentDetailView.as_view(),name='student_detail_view'),
    path('teachers/<int:id>/',TeacherDetailView.as_view(), name='teacher_detail_view'),
    path('classes/<int:id>/',ClassesDetailView.as_view(), name='classes_detail_view'),
    path('periods/<int:id>/',Class_PeriodDetailView.as_view(), name='class_period_detail_view'),
    path('courses/<int:id>/', CoursesDetailView.as_view(), name='courses_detail_view'),
]