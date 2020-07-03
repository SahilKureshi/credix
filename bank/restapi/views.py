from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import bank
from django.core import serializers
from .serializers import bankSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import JsonResponse
import json
# Create your views here.


@api_view(["POST"])
def bankinfo(request):
    # k = json.loads(request.data)
    data1=request.data
    print(data1['ifsc'])
    # print(k)
    # print(ifsc)
    banks = bank.objects.filter(ifsc = data1['ifsc'])
    ser = bankSerializer(banks,many = True)
    return Response(ser.data)


@api_view(["POST"])
def bankinfo_task(request):
    data2 = request.data
    
    banks = bank.objects.filter(bank_name = data2['bank_name'],city = data2['city'])

    ser = bankSerializer(banks,many=True)
    return Response(ser.data)