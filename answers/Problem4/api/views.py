from django.db import connections
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from django.http import HttpResponse, JsonResponse
from .data_records import WeatherDataRecords, YieldDataRecords
import psycopg2
from .serializer import WeatherDataRecordSerializer, YieldDataRecordSerializer


class GetAllWeatherRecords(ListAPIView):

    queryset = WeatherDataRecords.objects.all().order_by('date_of_day')[:10]
    serializer_class = WeatherDataRecordSerializer


class GetAllYieldData(ListAPIView):
    queryset = YieldDataRecords.objects.all()
    serializer_class = YieldDataRecordSerializer


def weather(request, req_year, weather_station_id):
    # text = weather_station_id.upper()
    # print(weather_station_id.upper())
    with connections['MYINTERVIEW'].cursor() as cursor:
        print('select * from data_analysis da where da.yr = {0} and da.station_id = {1};'.format(req_year, weather_station_id))
        cursor.execute("select * from data_analysis da where da.yr = '{0}' and da.station_id = '{1}';".format(req_year, weather_station_id))
        # cursor.execute("select * from myinterview.data_analysis da where da.yr = '1985' and da.station_id ='USC00121873'")
        result1 = cursor.fetchone()

    return JsonResponse(result1)

def yield_data(request):
    return JsonResponse({'data':'corn_harvest_in_US'})

def stats(request):
    return JsonResponse({'data':'stats'})