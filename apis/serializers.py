from rest_framework import serializers
from .models import School, Student, Teacher, Classroom

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

        def validate(self, data):
            if School.objects.filter(name=data['name'], address=data['address']).exists():
                raise serializers.ValidationError('School with this name and address already exists.')
            return data
        
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SchoolDetailSerializer(serializers.ModelSerializer):
    classrooms_count = serializers.SerializerMethodField()
    teachers_count = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ('id', 'name', 'address', 'classrooms_count', 'teachers_count', 'students_count')
        
class ClassroomDetailSerializer(serializers.ModelSerializer):
    classrooms_count = serializers.SerializerMethodField()
    teachers_count = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()



class TeacherDetailSerializer(serializers.ModelSerializer):
    classrooms_count = serializers.SerializerMethodField()
    teachers_count = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()


class StudentDetailSerializer(serializers.ModelSerializer):
    classrooms_count = serializers.SerializerMethodField()
    teachers_count = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ('id', 'name', 'address', 'classrooms_count', 'teachers_count', 'students_count')

    def get_classrooms_count(self, obj):
        return Classroom.objects.filter(school=obj).count()

    def get_teachers_count(self, obj):
        return Teacher.objects.filter(school=obj).count()

    def get_students_count(self, obj):
        return Student.objects.filter(school=obj).count()
