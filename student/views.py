
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import Student
from apis.serializers import StudentDetailSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from apis.filters import StudentFilter

class StudentCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)
    
class StudentFind(APIView):
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter

    def get(self, request):
        Students = Student.objects.filter()  
        filterset = self.filterset_class(request.GET, queryset=Students) 
        serializer = StudentSerializer(filterset.qs, many=True)
        return Response(serializer.data)
    
class StudentDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            Student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentDetailSerializer(Student)
        return Response(serializer.data)

class StudentUpdateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        Student = Student.objects.get(name=request.data['old-Student'])
        new_detail = request.data['new-detail']
        serializer = StudentSerializer(Student, data=new_detail, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class StudentDelete(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            Student = Student.objects.get(name=request.data['name'])
            Student.delete()
            Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)