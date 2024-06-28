# from django_filters import FilterSet, filters
from django_filters import rest_framework as filters
from apis.models import School, Classroom, Teacher, Student

class SchoolFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']

class ClassroomFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Classroom
        fields = ['name']

class TeacherFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ['name']

class StudentFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['name']