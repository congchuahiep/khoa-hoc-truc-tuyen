from rest_framework.serializers import ModelSerializer
from .models import Category, Course, Lesson, Tag, Comment, User

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ModelWithImageSerializer(ModelSerializer):
    # this function run before serialization time
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # change raw image to cloudinary url
        data['image'] = instance.image.url if instance.image else ''
        return data


class CourseSerializer(ModelWithImageSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'description', 'image']


class LessonSerializer(ModelWithImageSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'content', 'image']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']


class CommentSerializer(ModelSerializer):
    # let comment know how to display user
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_date', 'updated_date', 'user']


class LessonDetailSerializer(LessonSerializer):
    # let lesson know how to display tags
    tags = TagSerializer(many=True)

    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content', 'tags']
