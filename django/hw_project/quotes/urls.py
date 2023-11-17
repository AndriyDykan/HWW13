
from django.contrib import admin
from django.urls import path
from . import views

app_name = "quotes"
urlpatterns = [
    path("", views.main,name="root"),
    path("<int:page>", views.main,name="root_paginate"),
    path("tag/", views.tag,name="tag"),
    path("author/", views.author,name="author"),
    path("quote/", views.quote,name="quote"),
    path('detail/<int:author_id>', views.detail, name='detail'),

]
