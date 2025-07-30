from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField()

    def __str__(self):
        return f'게시글 제목은 {self.title} - 게시글 내용은 {self.content}.'




