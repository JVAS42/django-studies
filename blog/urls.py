from django.urls import path

from . import views

# http://seudominio.com.br/blog/
urlpatterns = [
    path('', views.blog),
    path('exemplos/', views.blog)
]