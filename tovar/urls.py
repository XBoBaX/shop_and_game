from django.urls import path
from . import views

urlpatterns = [
    path('games/select/', views.select),
    path('games/src/', views.src),
    path('games/buy/', views.buy),
    path('games/', views.podbor),
    path('my/', views.reg),
    path('my/vh', views.vhod),
    path('my/login/', views.Tologin),
    path('my/profile/', views.profile),
    path('my/logout/', views.logout),
    path('src/', views.compex),
    path('srcin/', views.compex),
    path('more/', views.more),

    path('auth/register/', views.register),

    path('', views.main),
]
