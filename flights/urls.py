from django.urls import path
from .views import FlightJourneyListView

urlpatterns = [
    path('flight-journey/', FlightJourneyListView.as_view(), name='flight-journey-list'),
]
