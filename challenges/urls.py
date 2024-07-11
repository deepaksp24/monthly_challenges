from django.urls import path

from . import views

urlpatterns = [
    # path("jan", views.january),
    # path("feb", views.february),
    # path("mar", views.march),
    path("", views.index),  # /challeneges/
    path("<int:month>", views.mothly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
