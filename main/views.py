# from django.shortcuts import render
from .serializer import StudentsSerializer
# from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from .models import *
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404


# Create your views here.

# class StudentView(ViewSet):

    # def list(self, request):
    #     queryset = Students.objects.all()
    #     serializer = StudentsSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Students.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = StudentsSerializer(user)
    #     return Response(serializer.data)

class StudentView(ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()