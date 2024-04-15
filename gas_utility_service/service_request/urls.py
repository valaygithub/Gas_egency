from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home,name="home"),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_request, name='track_request'),

    path('register',views.register,name="user_register"),
    path('login',views.user_login,name="user_login"),
    path('logout',views.user_logout,name="user_logout"),
]
