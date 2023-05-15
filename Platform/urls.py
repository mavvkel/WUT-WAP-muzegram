from django.urls import path
from . import views
from .views import profile_list, profile, register

app_name = 'Platform'

urlpatterns = [
    path('', views.FeedView.as_view(), name='feed'),
    path('profile-list/', profile_list, name='profile-list'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('register/', register, name='register'),
]
