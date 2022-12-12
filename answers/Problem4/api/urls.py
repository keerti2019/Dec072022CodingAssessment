from django.urls import path
from . import views

urlpatterns = [
    path("weather/", views.GetAllWeatherRecords.as_view()),
    path("yield/", views.GetAllYieldData.as_view()),
    path("weather/stats/<str:req_year>/<str:weather_station_id>",views.weather),
]

# testurls
# http://127.0.0.1:8000/api/weather
# http://127.0.0.1:8000/api/yield
# http://127.0.0.1:8000/api/weather/stats/1985/USC00121873
# 1985-2014/
