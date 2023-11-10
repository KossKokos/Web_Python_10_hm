
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signupuser, name='register'),
    path('login/', views.signinuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
]