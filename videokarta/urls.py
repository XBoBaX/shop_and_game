from django.urls import path
from . import views

urlpatterns = [
    path('upd/', views.update),
    path('pr/', views.price),
]
