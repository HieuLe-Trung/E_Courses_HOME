from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    # avatar = models.ImageField(upload_to='uploads/%Y/%m', default=None)
    avatar = models.ImageField(upload_to='postImageCourse')


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class itemBase(models.Model):  # tạo lớp abstract(các lớp có trường chung dùng)
    class Meta:
        abstract = True

    subject = models.CharField(max_length=100, null=False)
    # image = models.ImageField(upload_to='uploads/%Y/%m', default=None)
    image = models.ImageField(upload_to='postImageCourse')
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject


class Course(itemBase):
    class Meta:
        unique_together = ('subject', 'category')  # category không chứa các course trùng tên

    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


class Lesson(itemBase):
    class Meta:
        unique_together = ('subject', 'course')

    content = RichTextField()
    course = models.ForeignKey(Course, related_name="lessons",
                               on_delete=models.CASCADE)  # khi xóa Course thì các lesson bị xóa
    # 1 bài học có nhìu tag
    tags = models.ManyToManyField('tag', blank=True, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Interaction(itemBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Like(Interaction):
    # like theo kiểu facebook
    class Meta:
        unique_together = ("lesson", "user")


class Comment(Interaction):
    content = models.CharField(max_length=255)
