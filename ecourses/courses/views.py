from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from courses import serializers, paginators


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    pagination_class = paginators.CoursePaginator

    @action(methods=['get'], detail=True)
    def get_lessons(self, request, pk):  # pk: id truyền vào
        lessons = self.get_object().lessons.filter(
            active=True).all()  # .lessons. này là khóa ngoại của course có related_name

        return Response(serializers.LessonSerializer(lessons, many=True).data)  # trả về nhiều nên many=True


class LessonViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Lesson.objects.filter(active=True).all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        queries = self.queryset  # lấy những bài học đã active

        q = self.request.query_params.get("q")  # khi search /?q=... thì lấy giá trị q về
        if q:
            queries = queries.filter(subject__icontains=q)

        return queries


def index(request):
    return HttpResponse("Hello world!!!!")


def WELCOME(request, year):  # tham số year được truyền từ urls của app
    return HttpResponse("WELCOME" + str(year))


def WELCOME2(request, year):
    return HttpResponse("WELCOME " + str(year))
