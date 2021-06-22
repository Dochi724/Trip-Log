from os import name
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('create_profile', views.create_profile, name="create_profile"),
    #path('modify_profile', views.modify_profile, name='modify_profile'),
    path('modify_profile/<int:pk>',
    views.modify_profile, name='modify_profile'),
]
