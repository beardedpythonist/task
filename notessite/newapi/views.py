from rest_framework.generics import ListCreateAPIView
from main.models import Task
from rest_framework.viewsets import ModelViewSet
from .serializer import TaskSerializer


class PostViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()



