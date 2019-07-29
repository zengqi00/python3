from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)  #创建一个自增长的主键
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=50)
    active = models.CharField(max_length=2)

class BlogsPost(models.Model):
    title = models.CharField(max_length=150)  #博客标题
    body = models.TextField() #博客正文
    create_time =models.DateTimeField() # 创建时间