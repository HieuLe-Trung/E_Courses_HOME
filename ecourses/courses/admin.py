from django.contrib import admin
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


class LessonTagInlineAdmin(admin.TabularInline):  # trong Lesson có nhiều tag, add các tag liên quan VÀ TRONG CÁC TAG CÓ NHIỀU LESSON
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

# Register your models here.
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)  # trong khóa học hện các bài học liên quan
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag,TagAdmin)
