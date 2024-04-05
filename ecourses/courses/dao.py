#truy vấn dữ liệu

from .models import Course,Category

def load_courses(params={}):
    q = Course.objects.filter(active=True)#lấy ra những khóa học đã active

    kw = params.get('kw')
    if kw:
        q = q.filter(subject_contains=kw)

    cate_id = params.get('cate_id')
    if cate_id:
        q = q.filter(category_id=cate_id)

    return q