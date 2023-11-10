from django.contrib import admin
from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('author/<str:author>', views.get_author, name='get_author'),
    path('add/quote', views.add_quote, name='add_quote'),
    path('add/author', views.add_author, name='add_author'),
    path('add/tag', views.add_tag, name='add_tag'),
    path('delete/author', views.delete_author, name='delete_author'),
    path('delete_quote/<int:quote_id>', views.delete_quote, name='delete_quote'),
    path('delete/tag', views.delete_tag, name='delete_tag'),
    path('tag/<str:tag>/page/<int:page>', views.get_tag, name='get_tag'),
]