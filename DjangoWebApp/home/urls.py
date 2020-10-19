from django.urls import path
from . import views
from home.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('home/', views.home_view, name='home_view')
]