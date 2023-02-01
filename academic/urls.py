from django.urls import path
from .views import StudentList, StudentDetail, TeacherList, TeacherDetail, ClassList, ClassDetail, AssignmentList, AssignmenDetail

urlpatterns = [
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-details'),
    path('teachers/', TeacherList.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher-details'),
    path('classes/', ClassList.as_view(), name='class-list'),
    path('classes/<int:pk>/', ClassDetail.as_view(), name='class-details'),
    path('assignments/', AssignmentList.as_view(), name='assignment-list'),
    path('assignments/<int:pk>/', AssignmenDetail.as_view(), name='assignment-details'),
]