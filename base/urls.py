from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name="book-list"),
    path('login/', views.UserLoginView.as_view(), name="user-login"),
    path('register/', views.UserRegistrationView.as_view(), name="user-register"),
]
