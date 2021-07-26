from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create, name="create_cbtuser"),
    path('login/', views.login_cbtuser, name="login_cbtuser"),
    path('aaa/', views.logout_cbtuser, name="logout_cbtuser"),
]