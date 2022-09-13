from django.urls import path
from . import views


# app name for the purpose of referencing in templates.
app_name = 'users'


urlpatterns = [
    path('', views.root, name='root'),
    path('users', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('users/new', views.register, name='new'),
]