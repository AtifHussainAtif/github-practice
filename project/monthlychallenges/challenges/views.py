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
       return HttpResponse(challenges_text)
    except:
        return HttpResponseNotFound("wrong month")