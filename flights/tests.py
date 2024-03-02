from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from .models import Flight, FlightJourney
from django.utils import timezone
from datetime import timedelta

class FlightJourneyListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data for flights and flight journeys
        flight = Flight.objects.create(flight_number="AB123", airline_name="TestAir")
        FlightJourney.objects.create(
            flight=flight,
            source_city="CityA",
            destination_city="CityB",
            departure_time=timezone.now() + timedelta(days=1),
            arrival_time=timezone.now() + timedelta(days=1, hours=2),
            duration=timedelta(hours=2),
            no_of_stops=0,
            price=100.00
        )

    def test_filter_filter(self):
        url = reverse('flight-journey-list')
        response = self.client.get(url, {'source_city': 'citya', 'destination_city': 'cityb', 'travel_date': (timezone.now() + timedelta(days=1)).date()})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)  # Assuming the filter is case-insensitive


    def test_invalid_filter(self):
        url = reverse('flight-journey-list')
        response = self.client.get(url, {'source_city': 'citya', 'destination_city': 'cityb'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(len(response.data) > 0)  # Assuming the filter is case-insensitive
