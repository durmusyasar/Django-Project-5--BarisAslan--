# -*- coding: utf-8 -*-
from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('index/', post_index, name='index'),
    path('<slug>/detail/', post_detail, name='detail'),
    path('create/', post_create, name='create'),
    path('<slug>/update/', post_update, name='update'),
    path('<slug>/delete/', post_delete, name='delete'),
]