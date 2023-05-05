from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), #GET
    path('about/', views.about_us, name="about_us"),
    path('articles/', views.articles, name="articles"),

]