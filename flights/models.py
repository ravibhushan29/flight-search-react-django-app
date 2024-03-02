from django.db import models

from common.models import BaseModel


class Flight(BaseModel):
    flight_number = models.CharField(max_length=10, unique=True)
    airline_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.airline_name} - {self.flight_number}"


class FlightJourney(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='journeys')
    source_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.DurationField()
    no_of_stops = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.flight} from {self.source_city} to {self.destination_city} at {self.departure_time.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        indexes = [
            models.Index(fields=['source_city', 'destination_city', 'departure_time']),
        ]



