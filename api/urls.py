from django.urls import path
from . import views
urlpatterns=[
    path('todos/completed', views.TodoCompleted.as_view()),
]