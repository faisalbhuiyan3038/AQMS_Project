from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage_view, name='LoginPage')
]
