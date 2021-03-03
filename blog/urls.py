from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.article, name="list"),
]
