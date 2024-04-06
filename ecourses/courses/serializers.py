from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Course, Lesson, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course  # tương tac với model Course
        fields = ["id", "subject", "image", "created_date", "category"]
