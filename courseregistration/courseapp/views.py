from courseapp.models import Course
from studentapp.models import Student
from .serializers import CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from courseapp import serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CourseApi (APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id=None, format=None):
        if id is not None:
            course = Course.objects.get(id = id)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializers = CourseSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, format=None):
        course = Course.objects.get(id = id)
        serializers = CourseSerializer(course, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id, format=None):
        course = Course.objects.get(id = id)
        serializers = CourseSerializer(course, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        course = Course.objects.get(id = id)
        course.delete()
        return Response({'response': 'Course deleted successfully'})