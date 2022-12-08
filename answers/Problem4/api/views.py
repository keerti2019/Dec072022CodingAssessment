from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse


def weather(request):
    return JsonResponse({'data':'weather'})

def yield_data(request):
    return JsonResponse({'data':'corn_harvest_in_US'})

def stats(request):
    return JsonResponse({'data':'stats'})
