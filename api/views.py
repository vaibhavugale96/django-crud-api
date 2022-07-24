from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView


class StudentList(ListAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer

class StudentCreate(CreateAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer
    
class StudentUpdate(UpdateAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer
    
    
class StudentDelete(DestroyAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer
    lookup_field = 'id'