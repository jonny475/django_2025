from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)

    def __str__(self):
        return f'{self.name}---{self.slug}'

    def get_url(self):
        return f'/blog/category/{self.slug}/'



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    uploaded_image = models.ImageField(upload_to='images/', blank=True)
    uploaded_file = models.FileField(upload_to='files/', blank=True)
    downloaded_file = models.FileField(upload_to='files/', blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'게시글 제목은 {self.title} - by {self.author} - category {self.category} - 게시글 내용은 {self.content} - 생성 시간 {self.update_date} - 수정 시간 {self.update_date}'

