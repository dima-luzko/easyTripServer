from django.shortcuts import render
from api.serialization import *
from api.models import *
from rest_framework import generics
from rest_framework.decorators import api_view

# Create your views here.

class CardByNameView(generics.ListAPIView):
    serializer_class = ser_card

    def get_queryset(self):
        return card.objects.filter(number=self.kwargs['card_number']).distinct()

class TransportView(generics.ListAPIView):
    queryset = transport.objects.all()
    serializer_class = ser_transport

class TransportIdView(generics.RetrieveAPIView):
    queryset = transport.objects.all().order_by('name')
    serializer_class = ser_transport

class TransactionsOfCardView(generics.ListAPIView):
    serializer_class = ser_transaction

    def get_queryset(self):
        return transaction.objects.filter(card_id=self.kwargs['card']).distinct()

class NumberOfDaysView(generics.ListAPIView):
    queryset = number_of_day.objects.all()
    serializer_class = ser_number_of_day

class NumberOfTripsView(generics.ListAPIView):
    queryset = number_of_trip.objects.all()
    serializer_class = ser_number_of_trip

class NumberOfDaysTarifView(generics.ListAPIView):
    serializer_class = ser_tarif

    def get_queryset(self):
        return tarif.objects.filter(number_of_day_id=self.kwargs['number_of_day_id']).distinct()

    