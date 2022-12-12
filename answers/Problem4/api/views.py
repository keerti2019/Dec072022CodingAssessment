from django.db import connections
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from django.http import HttpResponse, JsonResponse
from .data_records import WeatherDataRecords, YieldDataRecords
import psycopg2
from .serializer import *


class GetAllWeatherRecords(ListAPIView):
    queryset = WeatherDataRecords.objects.all().order_by('date_of_day')[:10]
    serializer_class = WeatherDataRecordSerializer


class GetAllYieldData(generics.ListAPIView):
    queryset = YieldDataRecords.objects.all()
    serializer_class = YieldDataRecordSerializer

    def get_queryset(self):
        username = self.kwargs['year']
        return YieldDataRecords.objects.filter(year=username).only('year', 'total_harvest_corn_mt')


class WeatherStats(generics.ListAPIView):
    serializer_class = DataAnalysisSerializer

    def get_queryset(self):
        username = self.kwargs['yr']
        station = self.kwargs['station_id']
        return DataAnalysis.objects.filter(yr=username, station_id=station).only('yr', 'station_id', 'avg_max_temp', 'avg_min_temp', 'accum_preciptn')

