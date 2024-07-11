from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


# def january(request):
#     return HttpResponse("full motivation month")


# def february(request):
#     return HttpResponse("walk atleast 20minutes a day")


# def march(request):
#     return HttpResponse("focus on yourself")

def index(request):
    list_items = ""
    months = list(mothly_challenges.keys())
    for month in months:
        captitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href= \"{month}\">{captitalized_month}</a></li>"
    response_data = f"<ol>{list_items}</ol>"
    return HttpResponse(response_data)


mothly_challenges = {
    "jan": "full motivation",
    "feb": "starting a workouts",
    "mar": "walking",
    "apr": "breathing",
}


def mothly_challenge_by_number(request, month):
    months = list(mothly_challenges.keys())
    forward_months = months[month-1]
    redirect_path = reverse("month-challenge", args=[forward_months])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = mothly_challenges[month]
        respose_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(respose_data)
    except:
        return HttpResponse("<h1>this month is not supported</h1>")
