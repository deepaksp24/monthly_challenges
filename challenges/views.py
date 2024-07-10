from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


# def january(request):
#     return HttpResponse("full motivation month")


# def february(request):
#     return HttpResponse("walk atleast 20minutes a day")


# def march(request):
#     return HttpResponse("focus on yourself")


def monthly_challenge(request, month):
    if month == 'january':
        challenge_test = "full motivation month"
    elif month == 'february':
        challenge_test = "walk atleast 20minutes a day"
    elif month == 'march':
        challenge_test = "do somthing produvtive"
    else:
        return HttpResponseNotFound("this month is not supported")
    return HttpResponse(challenge_test)
