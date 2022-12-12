from rest_framework import serializers
from .data_records import *


class WeatherDataRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherDataRecords
        fields = ['date_of_day', 'max_temp_degc', 'min_temp_degc', 'amnt_precipation_mm', 'weather_station']


class YieldDataRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = YieldDataRecords
        fields = ['year', 'total_harvest_corn_mt']


class DataAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnalysis
        fields = ['yr', 'station_id', 'avg_max_temp', 'avg_min_temp', 'accum_preciptn']

