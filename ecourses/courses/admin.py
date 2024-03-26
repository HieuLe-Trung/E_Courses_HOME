from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets \
    import CKEditorUploadingWidget
from .models import Course, Category, Lesson, Tag


class LessonForm(forms.ModelForm):  # tạo ra 1 form có thanh cong cụ như word
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonTagInlineAdmin(
    admin.TabularInline):  # trong Lesson có nhiều tag, add các tag liên quan VÀ TRONG CÁC TAG CÓ NHIỀU LESSON
    model = Lesson.tags.through


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'course']
    list_filter = ['subject', 'created_date']
    search_fields = ['subject', 'course__subject']
    readonly_fields = ["avatar"]
    form = LessonForm
    inlines = [LessonTagInlineAdmin, ]

    def avatar(self, lesson):
        return mark_safe('''
        <img src='/static/{img_url}' alt='{alt}' width='120px' />
        '''.format(img_url=lesson.image.name, alt=lesson.subject))


class LessonInlineAdmin(admin.StackedInline):
    model = Lesson
    fk_name = 'course'  # tên khóa ngoại trong Models Lesson có course


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInlineAdmin, ]


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [LessonTagInlineAdmin]


class CourseAppAdminSite(admin.AdminSite):
    site_title = 'Trang quản trị của tôi'
    site_header = 'Hệ thống khóa học trực tuyến'
    index_title = 'Trang chủ quản trị'

    def get_urls(self):
        return [path('course-stats/', self.stats_view)] + super().get_urls()#/course-stats để render ra trang course-stats.html

    def stats_view(self, request):  # Thêm tham số 'request' vào đây
        course_count = Course.objects.count()
        #đếm mỗi khóa học có bao nhiêu bài học:
        stats = Course.objects.annotate(lesson_count=Count('lessons')).values('id','subject','lesson_count')
        return TemplateResponse(request, 'admin/course-stats.html',
                                {'course_count': course_count,# truyền số Course vào template
                                         'course_stats':stats})


admin_site = CourseAppAdminSite(name='mycourse')

# Register your models here.
admin_site.register(Category)
admin_site.register(Course, CourseAdmin)  # trong khóa học hện các bài học liên quan
admin_site.register(Lesson, LessonAdmin)
admin_site.register(Tag, TagAdmin)
