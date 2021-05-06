from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookview, name='home')
]
