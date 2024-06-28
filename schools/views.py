
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import School
from apis.serializers import SchoolDetailSerializer, SchoolSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from apis.filters import SchoolFilter

class SchoolCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SchoolList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)
    
class SchoolFind(APIView):
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter

    def get(self, request):
        schools = School.objects.filter()  
        filterset = self.filterset_class(request.GET, queryset=schools) 
        serializer = SchoolSerializer(filterset.qs, many=True)
        return Response(serializer.data)
    
class SchoolDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            school = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SchoolDetailSerializer(school)
        return Response(serializer.data)

class SchoolUpdateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        school = School.objects.get(name=request.data['old-school'])
        new_detail = request.data['new-detail']
        serializer = SchoolSerializer(school, data=new_detail, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class SchoolDelete(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            school = School.objects.get(name=request.data['name'])
            school.delete()
            Response(status=status.HTTP_204_NO_CONTENT)
        except School.DoesNotExist:
            return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)