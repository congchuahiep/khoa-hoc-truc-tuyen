from django.urls import path, include
from . import views
from rest_framework import routers

# register url route
router = routers.DefaultRouter()
router.register('categories', viewset=views.CategoryViewSet, basename="category")
router.register('courses', viewset=views.CourseViewSet, basename="course")
router.register('lessons', viewset=views.LessonViewSet, basename="lesson")
router.register('users', viewset=views.UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
]
