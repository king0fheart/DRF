from django.http import JsonResponse
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api import serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskApi (APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id=None, format=None):
        if id is not None:
            task = Task.objects.get(id = id)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializers = TaskSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, format=None):
        task = Task.objects.get(id = id)
        serializers = TaskSerializer(task, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id, format=None):
        task = Task.objects.get(id = id)
        serializers = TaskSerializer(task, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        task = Task.objects.get(id = id)
        task.delete()
        return Response({'response': 'Task delete successfully'})


#Function based API

# # Create your views here.
# @api_view(['GET'])
# def api_overview(request):
#     return JsonResponse("API Base Point", safe=False)

# @api_view(['GET'])
# def taskList(request):
#     tasks = Task.objects.all()
#     serializers = TaskSerializer(tasks, many=True)
#     return Response(serializers.data)

# @api_view(['GET'])
# def taskDetail(request, pk):
#     tasks = Task.objects.get(id = pk)
#     serializers = TaskSerializer(tasks, many=False)
#     return Response(serializers.data)

# @api_view(['POST'])
# def taskCreate(request):
#     serializers = TaskSerializer(data = request.data)
#     if serializers.is_valid():
#         serializers.save()
#         return Response(serializers.data)
#     return Response(serializers.error_messages)

# @api_view(['POST'])
# def taskUpdate(request, pk):
#     task = Task.objects.get(id = pk)
#     serializers = TaskSerializer(instance=task, data = request.data)
#     if serializers.is_valid():
#         serializers.save()
#         return Response(serializers.data)
#     return Response(serializers.error_messages)

# @api_view(['DELETE'])
# def taskDelete(request, pk):
#     task = Task.objects.get(id = pk)
#     task.delete()
#     return Response('Task delete successfully')