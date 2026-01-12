from django.urls import path

from . import views

# http://seudominio.com.br/
urlpatterns = [
    path('', views.home)
]