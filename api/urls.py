from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassroomListView
from .views import ClassPeriodListView
from .views import StudentDetailView
from .views import ClassPeriodDetailView
from .views import TeacherDetailView
from .views import CourseDetailView
from .views import ClassroomDetailView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list_view'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list_view'),
    path("classrooms/", ClassroomListView.as_view(), name = "classroom_list_view"),
    path('courses/', CourseListView.as_view(), name='courses_list_view'),
    path("class-periods/", ClassPeriodListView.as_view(), name = "class_period_list_view"),
    path('students/<int:id>/',StudentDetailView.as_view(),name='student_detail_view'),
    path('teachers/<int:id>/',TeacherDetailView.as_view(), name='teacher_detail_view'),
    path("classrooms/<int:id>/", ClassroomDetailView.as_view(),name="classroom_detail_view" ),
    path("class-periods/<int:id>/", ClassPeriodDetailView.as_view(),name="class_period_detail_view" ),
    path('courses/<int:id>/', CourseDetailView.as_view(), name='course_detail_view'),
]