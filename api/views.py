from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class TodoListView(APIView):
    def get(self,request,*args,**kwargs):
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset,many=True)

        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=201)
    
    def delete(self,request):
        pass

    def update(self,requet):
        pass