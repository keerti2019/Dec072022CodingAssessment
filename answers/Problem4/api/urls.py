from django.urls import path
from . import views

urlpatterns = [
    path("weather/", views.GetAllWeatherRecords.as_view()),
    path("yield/", views.yield_data, name='yield_data'),
    path("weather/stats/", views.stats),
]

# testurls
# http://127.0.0.1:8000/api/weather
# http://127.0.0.1:8000/api/yield
# http://127.0.0.1:8000/api/weather/stats
