from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'author', 'content', 'uploaded_image', 'uploaded_file']
