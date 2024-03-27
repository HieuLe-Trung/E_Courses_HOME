from django.urls import path, re_path
from . import views
from .admin import admin_site

urlpatterns = [
    path('',views.index, name="index"),
    path('welcome/<int:year>', views.WELCOME), #'welcome': định nghĩa url, còn WELCOME: render trang đó lên
    re_path(r'^welcome2/(?P<year>[0-9]{1,2})/$', views.WELCOME2),#biểu thức chính quy 're_path'
    path('admin/', admin_site.urls)
]