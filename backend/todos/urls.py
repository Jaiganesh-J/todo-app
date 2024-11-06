from django.urls import path

from .views import ListTodo, DetailTodo

urlpatterns - [
    path("<int:pk0\>/", DetailTodo.as_view()),
    path("", ListTodo.as_view()),
]
