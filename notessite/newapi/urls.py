from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from .views import PostViewSet


api_router = SimpleRouter()
api_router.register(r'task', PostViewSet)

urlpatterns = [
    path('v1/', include(api_router.urls)) #/api/v1/task
]