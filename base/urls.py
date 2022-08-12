from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
     path('', views.BookList.as_view(),name="book-list"),
]
