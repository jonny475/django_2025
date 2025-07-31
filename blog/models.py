from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    uploaded_image = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return f'게시글 제목은 {self.title} - 게시글 내용은 {self.content} - 생성 시간 {self.update_date} - 수정 시간 {self.update_date}'




