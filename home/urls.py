from django.urls import path
from . import views 

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('posts/', views.getPosts, name="notes"),
    path('posts/<str:pk>/', views.getPost, name="note"),
]
