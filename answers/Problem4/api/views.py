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


def weather(request):
    conn = psycopg2.connect(database="postgres", user="postgres", password="BlueSky@143", host="127.0.0.1",
                            port="8002")
    cursor = conn.cursor()
    cursor.execute('set search_path="myinterview";')
    cursor.execute('SELECT * FROM weather_data_records LIMIT 10 OFFSET 0')
    result1 = cursor.fetchall()
    print(result1)

    return JsonResponse(result1)


# def get_supplier_data(request, in_part_id):
#     id = in_part_id
#     data = []
#     for s in SupplierParts.objects.all():
#         if id == s.part_id:
#             rowObj = Supplier.objects.get(pk=int(s.supplier_id))
#             if str(rowObj.supplier_name) in data:
#                 continue
#             else:
#                 data.append(str(rowObj.supplier_name))
#
#                 # print(data)
#
#     if not data:
#         data.append("No Records Found !")
#
#     return HttpResponse(data)





def yield_data(request):
    return JsonResponse({'data':'corn_harvest_in_US'})

def stats(request):
    return JsonResponse({'data':'stats'})