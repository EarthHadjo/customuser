from django.urls import path
from customuser_app import views


urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('login/', views.loginview),
    path('logout/', views.logoutview),
    path('signup/', views.signup),
]