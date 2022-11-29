from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


monthly_challenges = {
    "january" : "this is january",
    "february": "this is february",
    "march": "this is march",
    "april" : "this is april",
    "may" : "this is may",
    "june" : "this is june",
    "july" : "this is june",
    "july" : "this is july",
    "august" : "this is august",
    "september" : "this is september",
    "october" : "this is october",
    "november" : "this is november",
    "december" : "this is december"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capatilized_month = month.capitalize()
        month_path = reverse("month-challenges", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capatilized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
       challenges_text = monthly_challenges[month]
       response_data = f"<h1>{challenges_text}</h1>"
       return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>this month is invalid</h1>")