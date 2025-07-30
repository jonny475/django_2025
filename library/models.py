from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=20)
    book_category = models.CharField(max_length=10)
    created_date = models.DateTimeField()

    def __str__(self):
        return f'책 이름은 {self.title} 저자는 {self.author} 입니다.'
    def get_absolute_url(self):
        return f'/library/{self.pk}/'