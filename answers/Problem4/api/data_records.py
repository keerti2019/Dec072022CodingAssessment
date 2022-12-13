# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django_filters import rest_framework as filters


class WeatherDataRecords(models.Model):
    date_of_day = models.DateField(primary_key=True)
    max_temp_degc = models.DecimalField(max_digits=65535, decimal_places=5, blank=True, null=True)
    min_temp_degc = models.DecimalField(max_digits=65535, decimal_places=5, blank=True, null=True)
    amnt_precipation_mm = models.DecimalField(max_digits=65535, decimal_places=5, blank=True, null=True)
    weather_station = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_data_records'


class YieldDataRecords(models.Model):
    year = models.IntegerField(primary_key=True)
    total_harvest_corn_mt = models.DecimalField(max_digits=65535, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yield_data_records'


class DataAnalysis(models.Model):
    yr = models.IntegerField(primary_key=True)
    station_id = models.CharField(max_length=200)
    avg_max_temp = models.DecimalField(max_digits=65535, decimal_places=5, blank=True, null=True)
    avg_min_temp = models.DecimalField(max_digits=65535, decimal_places=5, blank=True, null=True)
    accum_preciptn = models.DecimalField(max_digits=65535, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_analysis'
        unique_together = (('yr', 'station_id'),)




