from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('hangHoa/',views.hangHoa, name='hangHoa'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginPage, name="login"),
]