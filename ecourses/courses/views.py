from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from .models import Course,Lesson
from .serializers import CourseSerializer, LessonSerializer
from courses import serializers, paginators


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    pagination_class = paginators.CoursePaginator


class LessonViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Lesson.objects.filter(active=True).all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        queries = self.queryset #lấy những bài học đã active

        q = self.request.query_params.get("q")# khi search /?q=... thì lấy giá trị q về
        if q:
            queries = queries.filter(subject__icontains=q)

        return queries


def index(request):
    return HttpResponse("Hello world!!!!")


def WELCOME(request, year):  # tham số year được truyền từ urls của app
    return HttpResponse("WELCOME" + str(year))


def WELCOME2(request, year):
    return HttpResponse("WELCOME " + str(year))
