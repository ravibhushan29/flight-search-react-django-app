import os
import django
import random
from django.utils import timezone
from faker import Faker
from datetime import timedelta


# Import your models here
from flights.models import Flight, FlightJourney

# Initialize Faker
fake = Faker()

# Predefined list of airline names
airline_names = [
    "Delta Air Lines", "United Airlines", "American Airlines",
    "Southwest Airlines", "JetBlue Airways", "Alaska Airlines",
    "Spirit Airlines", "Frontier Airlines", "Hawaiian Airlines",
    "Allegiant Air", "SkyWest Airlines", "Air Canada",
    "British Airways", "Lufthansa", "Air France",
    "KLM Royal Dutch Airlines", "Qatar Airways", "Emirates",
    "Singapore Airlines", "Cathay Pacific", "ANA All Nippon Airways",
    "Etihad Airways", "Turkish Airlines", "EVA Air",
    "Virgin Atlantic", "Swiss International Air Lines", "Qantas Airways",
    "SAS Scandinavian Airlines", "Air New Zealand", "Aer Lingus",
    "Iberia", "Aeroflot", "Finnair", "LATAM Airlines", "EgyptAir"
]

# Predefined list of 10 cities
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"
]

def create_and_save_flights_and_journeys(num_flights, num_days):
    for _ in range(num_flights):
        flight_number = fake.unique.bothify(text='???###')
        airline_name = random.choice(airline_names)  # Select an airline name randomly from the list
        flight = Flight.objects.create(flight_number=flight_number, airline_name=airline_name)

        for _ in range(random.randint(1, 3)):  # Each flight has 1 to 3 journeys
            for day in range(num_days):
                # Ensure source and destination cities are not the same
                source_city, destination_city = random.sample(cities, 2)
                departure = timezone.now() + timedelta(days=day, hours=random.randint(0, 23), minutes=random.randint(0, 59))
                arrival = departure + timedelta(hours=random.randint(1, 5))
                FlightJourney.objects.create(
                    flight=flight,
                    source_city=source_city,
                    destination_city=destination_city,
                    departure_time=departure,
                    arrival_time=arrival,
                    duration=arrival - departure,
                    no_of_stops=random.randint(0, 2),
                    price=round(random.uniform(50.0, 500.0), 2)
                )

# Call the function with the desired number of flights and days
create_and_save_flights_and_journeys(30, 10)

print("Data generation and saving to database completed.")
