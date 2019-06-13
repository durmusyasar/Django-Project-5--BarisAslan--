# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Post, Comment
from captcha.fields import ReCaptchaField


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']

class CommentForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = [
            'name',
            'content',
        ]