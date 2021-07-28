from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_exam, name="create_exam")
]