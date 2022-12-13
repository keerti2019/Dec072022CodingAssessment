from django.db import connections
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from django.http import HttpResponse, JsonResponse
from .data_records import *
import psycopg2
from django_filters import rest_framework as filters
from .serializer import *


# For pagination
class GetAllWeatherRecords1(ListAPIView):
    queryset = WeatherDataRecords.objects.all().order_by('date_of_day')
    serializer_class = WeatherDataRecordSerializer


class GetAllWeatherRecords(generics.ListAPIView):
    serializer_class = WeatherDataRecordSerializer

    # queryset = WeatherDataRecords.objects.all()[:10]

    def get_queryset(self):
        username = self.kwargs['date_of_day']
        station = self.kwargs['weather_station']
        return WeatherDataRecords.objects.filter(date_of_day=username, weather_station=station).only('date_of_day',
                                                                                                     'max_temp_degc',
                                                                                                     'min_temp_degc',
                                                                                                     'amnt_precipation_mm',
                                                                                                     'weather_station')


class GetAllYieldData(generics.ListAPIView):
    serializer_class = YieldDataRecordSerializer

    def get_queryset(self):
        username = self.kwargs['year']
        return YieldDataRecords.objects.filter(year=username).only('year', 'total_harvest_corn_mt')

# Added pagination using query_parameters
class WeatherStats(generics.ListAPIView):
    serializer_class = DataAnalysisSerializer

    def get_queryset(self):
        req_kv = self.request.query_params
        start = req_kv['start']
        end = req_kv['end']
        if 'req_yr' in req_kv:
            req_yr = req_kv['req_yr']
        if 'station' in req_kv:
            station = req_kv['station']

        if 'req_yr' in req_kv and 'station' not in req_kv :
            return DataAnalysis.objects.filter(yr=req_yr).all()[int(start):int(end)]
        if 'req_yr' not in req_kv and 'station' in req_kv:
            return DataAnalysis.objects.filter(station_id=station).all()[int(start):int(end)]
        if 'req_yr' in req_kv and 'station' in req_kv:
            return DataAnalysis.objects.filter(station_id=station, yr=req_yr).only('yr', 'station_id', 'avg_max_temp', 'avg_min_temp', 'accum_preciptn')
        if 'req_yr' not in req_kv and 'station' not in req_kv:
            return DataAnalysis.objects.all()[int(start):int(end)]


