from django.urls import path
from . import views

urlpatterns =[path('', views.index),
              path('home/', views.index, name='home'),
              path('about/', views.about, name='about'),
              path('create/', views.create, name='create')
              ]



