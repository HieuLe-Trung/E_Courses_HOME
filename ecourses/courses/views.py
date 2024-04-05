from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets,generics
from .models import Course
from .serializers import CourseSerializer
from courses import serializers, paginators

class CourseViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    pagination_class = paginators.CoursePaginator

def index(request):
    return HttpResponse("Hello world!!!!")


def WELCOME(request, year):  # tham số year được truyền từ urls của app
    return HttpResponse("WELCOME" + str(year))


def WELCOME2(request, year):
    return HttpResponse("WELCOME " + str(year))
