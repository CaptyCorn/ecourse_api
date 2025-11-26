from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from courses import views

r = DefaultRouter()
r.register('categories', views.CategoryView, basename='category')
r.register('courses', views.CoureView, basename='course')

urlpatterns = [
    path('', include(r.urls)),
]