from django.urls import path

from . import views

urlpatterns = [
    # path("jan", views.january),
    # path("feb", views.february),
    # path("mar", views.march),
    path("<month>", views.monthly_challenge)
]
