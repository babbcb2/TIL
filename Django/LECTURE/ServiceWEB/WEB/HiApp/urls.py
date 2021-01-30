from django.contrib import admin
from django.urls import path, include
from HiApp    import views

urlpatterns = [
    # localhost:8000/Hiapp/index
    path('index/',      views.index),
    path('baseball/', views.baseball, name='base'),
    path('football/', views.football),
    path('basketball/', views.basketball),
    path('login/', views.login, name='msg'),
]