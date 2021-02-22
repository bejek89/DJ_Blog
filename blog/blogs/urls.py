# Definniuje wzorce adresów URL dla aplikacji blogs

from django.urls import path
from .import views

app_name = 'blogs'
urlpatterns = [
    # Strona główna
    path('', views.index, name='index'),
    ]