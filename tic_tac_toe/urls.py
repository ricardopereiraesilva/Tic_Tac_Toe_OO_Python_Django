from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_user>/', views.refresh, name='refresh'),
    path('<int:id_user>/<int:line>/<int:column>/', views.click, name='click'),
]