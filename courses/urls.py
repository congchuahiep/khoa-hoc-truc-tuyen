from django.urls import path, include, re_path
from . import views
from rest_framework import routers

from .admin import admin_site

# register url route
router = routers.DefaultRouter()
router.register('categories', viewset=views.CategoryViewSet, basename="category")
router.register('courses', viewset=views.CourseViewSet, basename="course")
router.register('lessons', viewset=views.LessonViewSet, basename="lesson")

urlpatterns = [
    path('', include(router.urls)),
]
