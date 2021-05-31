from django.shortcuts import render
from api.serialization import *
from api.models import *
from rest_framework import generics
from rest_framework.decorators import api_view
import simplejson as json
from django.http import HttpResponse, JsonResponse

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


class NumberOfDaysTarifView(generics.CreateAPIView):
    serializer_class = ser_tarif

    def post(self, request, *args, **kwargs):
        received_json_data = json.loads(request.body.decode("utf-8"))
        # queryset1 = transport.objects.filter(id__in=)
        queryset = tarif.objects.filter(number_of_day_id=received_json_data["number_of_day_id"],transports=received_json_data["transport"])
        data = [entry for entry in queryset.values()]
        json_data = json.dumps(data)

        return HttpResponse(json_data, content_type="application/json")