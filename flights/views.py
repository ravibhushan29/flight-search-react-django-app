from django_filters import rest_framework as filters
from rest_framework import generics, serializers
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny

from .models import FlightJourney
from .serializers import FlightJourneySerializer
from django_filters.filters import CharFilter, DateFilter


class FlightJourneyFilter(filters.FilterSet):
    source_city = CharFilter(field_name='source_city', lookup_expr='iexact')
    destination_city = CharFilter(field_name='destination_city', lookup_expr='iexact')
    travel_date = DateFilter(field_name='departure_time', lookup_expr='date')
    return_date = DateFilter(field_name='arrival_time', lookup_expr='date', required=False)

    class Meta:
        model = FlightJourney
        fields = []

    def __init__(self, *args, **kwargs):
        super(FlightJourneyFilter, self).__init__(*args, **kwargs)
        if 'travel_date' not in self.data:
            raise ValidationError({"error": "travel_date is required."})


class FlightJourneyListView(generics.ListAPIView):
    queryset = FlightJourney.objects.all()
    serializer_class = FlightJourneySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FlightJourneyFilter
    permission_classes = (AllowAny, )

    def get_queryset(self):
        """
        Enforces that source city, destination city, and travel date are provided.
        """
        queryset = super().get_queryset()
        source_city = self.request.query_params.get('source_city')
        destination_city = self.request.query_params.get('destination_city')

        if not source_city or not destination_city:
            raise ValidationError({"error": "Source City and Destination City are required."})

        return queryset
