import enrollment
import json
from enrollment.models import Enrollment
from .serializers import EnrollmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from studentapp.models import Student
from studentapp.serializers import StudentSerializer
from courseapp.models import Course
from courseapp.serializers import CourseSerializer

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

class EnrollmentApi (APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id=None, format=None):
        if id is not None:
            enrollment = Enrollment.objects.get(id = id)
            serializer = EnrollmentSerializer(enrollment)
            return Response(serializer.data)
        enrollments = Enrollment.objects.all()
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializers = EnrollmentSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, format=None):
        enrollment = Enrollment.objects.get(id = id)
        serializers = EnrollmentSerializer(enrollment, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id, format=None):
        enrollment = Enrollment.objects.get(id = id)
        serializers = EnrollmentSerializer(enrollment, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        enrollment = Enrollment.objects.get(id = id)
        enrollment.delete()
        return Response({'response': 'Student deleted successfully'})

class EnrolledStudentApi (APIView):
    def get(self, request, enroll_id=None, format=None):
        final_list = []
        if enroll_id is not None:
            course_enrollments = Enrollment.objects.filter(course_id=enroll_id)
            for x in course_enrollments:
                data = Student.objects.get(id = x.student.id)
                serializer = StudentSerializer(data)
                final_list.append(serializer.data)
            return Response(final_list)
        enrollments = Enrollment.objects.all()
        for x in enrollments:
            data = Student.objects.get(id = x.student.id)
            serializer = StudentSerializer(data)
            final_list.append(serializer.data)
        return Response(final_list)
    
    def post(self, request):
        insert_data = {
            'course': request.data[0]['course_id'],
            'student': request.data[0]['student_id'],
        }
        serializers = EnrollmentSerializer(data = insert_data)
        print(serializers)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)

class EnrolledCourseApi (APIView):
    def get(self, request, std_id=None, format=None):
        final_list = []
        if std_id is not None:
            course_enrollments = Enrollment.objects.filter(student_id=std_id)
            for x in course_enrollments:
                data = Course.objects.get(id = x.course.id)
                serializer = CourseSerializer(data)
                final_list.append(serializer.data)
            return Response(final_list)
        enrollments = Enrollment.objects.all()
        for x in enrollments:
            data = Course.objects.get(id = x.course.id)
            serializer = CourseSerializer(data)
            final_list.append(serializer.data)
        return Response(final_list)
    def post(self, request):
        insert_data = {
            'course': request.data[0]['course_id'],
            'student': request.data[0]['student_id'],
        }
        serializers = EnrollmentSerializer(data = insert_data)
        print(serializers)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
        
# function based view

# @api_view(('GET',))
# def get_enrolled_std_course(request, enroll_id):
#     # print(enroll_id)
#     # course_enrollments = Enrollment.objects.filter(course_id=enroll_id)
#     # serializer = EnrollmentSerializer(course_enrollments, many=True)
#     # return Response(serializer.data)

#     final_list = []
#     course_enrollments = Enrollment.objects.filter(course_id=enroll_id)
#     for x in course_enrollments:
#         data = Student.objects.get(id = x.student.id)
#         serializer = StudentSerializer(data)
#         final_list.append(serializer.data)
#     return Response(final_list)