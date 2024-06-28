"""
URL configuration for exam_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from schools.views import SchoolCreate, SchoolList, SchoolFind, SchoolDetailView, SchoolUpdateView, SchoolDelete
from classroom.views import ClassroomCreate, ClassroomList, ClassroomDelete, ClassroomUpdateView
from teacher.views import TeacherCreate, TeacherList, TeacherDelete, TeacherUpdateView
from student.views import StudentCreate, StudentList, StudentDelete, StudentUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apis.urls')),
    path('school/create', SchoolCreate.as_view()),
    path('school/list', SchoolList.as_view()),
    path('school/filter-name', SchoolFind.as_view()),
    path('school/<int:pk>', SchoolDetailView.as_view()),
    path('school/update', SchoolUpdateView.as_view()),
    path('school/delete', SchoolDelete.as_view()),
    path('classroom/create', ClassroomCreate.as_view()),
    path('classroom/list', ClassroomList.as_view()),
    path('classroom/update', ClassroomUpdateView.as_view()),
    path('classroom/delete', ClassroomDelete.as_view()),
    path('student/create', StudentCreate.as_view()),
    path('student/list', StudentList.as_view()),
    path('student/update', StudentUpdateView.as_view()),
    path('student/delete', StudentDelete.as_view()),
    path('teacher/create', TeacherCreate.as_view()),
    path('teacher/list', TeacherList.as_view()),
    path('teacher/update', TeacherUpdateView.as_view()),
    path('teacher/delete', TeacherDelete.as_view()),

]
