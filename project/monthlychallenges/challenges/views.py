from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def january(request):
    return HttpResponse("This Month is january")

def february(request):
    return HttpResponse("this month is february")


def monthly_challenge(request, month):
    return HttpResponse()