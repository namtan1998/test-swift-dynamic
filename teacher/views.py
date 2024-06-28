
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import Teacher
from apis.serializers import TeacherDetailSerializer, TeacherSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from apis.filters import TeacherFilter

class TeacherCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeacherList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        Teachers = Teacher.objects.all()
        serializer = TeacherSerializer(Teachers, many=True)
        return Response(serializer.data)
    
class TeacherFind(APIView):
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter

    def get(self, request):
        Teachers = Teacher.objects.filter()  
        filterset = self.filterset_class(request.GET, queryset=Teachers) 
        serializer = TeacherSerializer(filterset.qs, many=True)
        return Response(serializer.data)
    
class TeacherDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            Teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherDetailSerializer(Teacher)
        return Response(serializer.data)

class TeacherUpdateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        Teacher = Teacher.objects.get(name=request.data['old-Teacher'])
        new_detail = request.data['new-detail']
        serializer = TeacherSerializer(Teacher, data=new_detail, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class TeacherDelete(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            Teacher = Teacher.objects.get(name=request.data['name'])
            Teacher.delete()
            Response(status=status.HTTP_204_NO_CONTENT)
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)