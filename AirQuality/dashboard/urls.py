from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('',views.index,name='index'),
    path('create_air_quality_data/',views.StationAirQualityCreate.as_view(),name='create_air_quality_data'),
    path('create_route_wise_data',views.RouteWiseDataCreate.as_view(),name='create_route_wise_data'),
    path('signup/',views.SignUpView.as_view(),name='signup')
]
