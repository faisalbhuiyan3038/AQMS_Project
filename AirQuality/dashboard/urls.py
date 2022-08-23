from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('',views.index,name='index'),
    path('create_air_quality_data/',views.StationAirQualityCreate.as_view(),name='create_air_quality_data')
]
