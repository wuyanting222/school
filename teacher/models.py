from django.db import models


class Teacher(models.Model):
    _id = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, default='', max_length=100)  #名字
    age = models.IntegerField(null=False, default=30)  # 年龄

    class Meta:
        db_table = 'teacher'