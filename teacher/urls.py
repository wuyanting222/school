from django.conf.urls import url

from teacher.views import TeacherCreate

urlpatterns = [
    # url(r'^create', CourseCreate.as_view()),
    # url(r'^list', CourseList.as_view()),
    url(r'^create', TeacherCreate.as_view()),
]