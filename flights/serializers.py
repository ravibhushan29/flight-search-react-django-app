from rest_framework import serializers
from .models import Flight, FlightJourney


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['flight_number', 'airline_name']


class FlightJourneySerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)

    class Meta:
        model = FlightJourney
        fields = ['id', 'flight', 'source_city', 'destination_city', 'departure_time', 'arrival_time', 'duration',
                  'no_of_stops', 'price']
