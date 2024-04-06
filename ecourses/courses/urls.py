from django.urls import path, re_path, include
from . import views
from .admin import admin_site
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses',views.CourseViewSet)
router.register('lessons',views.LessonViewSet,basename='lessons')
router.register('lesson',views.LessonViewSet2,basename='lesson')
router.register('user',views.UserViewSet)

urlpatterns = [
    path('',include(router.urls), name="index"),
    path('welcome/<int:year>', views.WELCOME), #'welcome': định nghĩa url, còn WELCOME: render trang đó lên
    re_path(r'^welcome2/(?P<year>[0-9]{1,2})/$', views.WELCOME2),#biểu thức chính quy 're_path'
    path('admin/', admin_site.urls)
]