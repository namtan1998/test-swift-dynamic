
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import Classroom
from apis.serializers import ClassroomDetailSerializer, ClassroomSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from apis.filters import ClassroomFilter

class ClassroomCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassroomList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        Classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(Classrooms, many=True)
        return Response(serializer.data)
    
class ClassroomFind(APIView):
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter

    def get(self, request):
        Classrooms = Classroom.objects.filter()  
        filterset = self.filterset_class(request.GET, queryset=Classrooms) 
        serializer = ClassroomSerializer(filterset.qs, many=True)
        return Response(serializer.data)
    
class ClassroomDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            Classroom = Classroom.objects.get(pk=pk)
        except Classroom.DoesNotExist:
            return Response({'error': 'Classroom not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClassroomDetailSerializer(Classroom)
        return Response(serializer.data)

class ClassroomUpdateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        Classroom = Classroom.objects.get(name=request.data['old-Classroom'])
        new_detail = request.data['new-detail']
        serializer = ClassroomSerializer(Classroom, data=new_detail, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class ClassroomDelete(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            Classroom = Classroom.objects.get(name=request.data['name'])
            Classroom.delete()
            Response(status=status.HTTP_204_NO_CONTENT)
        except Classroom.DoesNotExist:
            return Response({'error': 'Classroom not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)