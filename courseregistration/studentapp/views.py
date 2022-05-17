from studentapp.models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from studentapp import serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentApi (APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id=None, format=None):
        if id is not None:
            student = Student.objects.get(id = id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializers = StudentSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, format=None):
        student = Student.objects.get(id = id)
        serializers = StudentSerializer(student, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id, format=None):
        student = Student.objects.get(id = id)
        serializers = StudentSerializer(student, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        student = Student.objects.get(id = id)
        student.delete()
        return Response({'response': 'Student deleted successfully'})