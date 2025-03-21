from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
import rest_framework.status
from rest_framework.decorators import action

from courses import paginators
from .models import Category, Course, Lesson, Comment
from .serializers import CategorySerializer, CourseSerializer, LessonSerializer, LessonDetailSerializer, \
    CommentSerializer


# Use ListAPIView for listing view
# Use RetrieveAPIView for detail view


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = paginators.ItemPagination
    permission_classes = [permissions.IsAuthenticated]

    # make query by id and query by category_id
    def get_queryset(self):
        query = self.queryset

        q = self.request.query_params.get('q')
        if q:
            query = query.filter(subject__icontains=q)

        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            query = query.filter(category_id=cate_id)

        return query

    # make a detail child url like /courses/{course_id}/lessons/?q=
    @action(methods=['get'], detail=True, url_name='lessons')
    def get_lessons(self, request, pk):
        lesson = self.get_object().lesson_set.filter(active=True)
        return Response(LessonSerializer(lesson, many=True).data, status=rest_framework.status.HTTP_200_OK)


class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.prefetch_related('tags').filter(active=True)
    serializer_class = LessonDetailSerializer

    # make a detail child url like /courses/{course_id}/lessons/?q=
    @action(methods=['get'], detail=True, url_name='comments')
    def get_comments(self, request, pk):
        # idk select_related does??!???
        comment = self.get_object().comment_set.select_related('user').filter(active=True)
        return Response(CommentSerializer(comment, many=True).data, status=rest_framework.status.HTTP_200_OK)
