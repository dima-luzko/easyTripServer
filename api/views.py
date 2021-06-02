from django.db.models import query
from api.serialization import *
from api.models import *
from rest_framework import generics
import json
import jsonpickle
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def NumberOfDaysTarif(request):
     if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        result = []
        transports = received_json_data["transports"]
        sql_list = str(tuple([key for key in transports])).replace(',)', ')')
        for row in tarif.objects.raw('''
        SELECT * FROM api_tarif 
        INNER JOIN api_tarif_transports ON api_tarif.id = api_tarif_transports.tarif_id 
        INNER JOIN api_transport ON api_tarif_transports.transport_id = api_transport.id 
        WHERE api_tarif.number_of_day_id_id = %s
        AND api_transport.id in {sql_list}
        AND api_tarif.id
        NOT IN (SELECT tarif_id FROM api_tarif_transports WHERE transport_id NOT IN {sql_list})
        GROUP BY api_tarif.id
        HAVING COUNT(*) = %s
        '''.format(sql_list=sql_list), [received_json_data["number_of_day_id"], received_json_data["count"]]):

           result.append({"price": row.price})
        json_data = json.dumps(result, cls=DjangoJSONEncoder)
        json_data1 = jsonpickle.decode(json_data)
        return HttpResponse(json_data1, content_type="application/json")

@csrf_exempt
def NumberOfTripTarif(request):
     if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        result = []
        transports = received_json_data["transports"]
        sql_list = str(tuple([key for key in transports])).replace(',)', ')')
        for row in tarif.objects.raw('''
        SELECT * FROM api_tarif 
        INNER JOIN api_tarif_transports ON api_tarif.id = api_tarif_transports.tarif_id 
        INNER JOIN api_transport ON api_tarif_transports.transport_id = api_transport.id 
        WHERE api_tarif.number_of_trip_id_id = %s
        AND api_transport.id in {sql_list}
        AND api_tarif.id
        NOT IN (SELECT tarif_id FROM api_tarif_transports WHERE transport_id NOT IN {sql_list})
        GROUP BY api_tarif.id
        HAVING COUNT(*) = %s
        '''.format(sql_list=sql_list), [received_json_data["number_of_trip_id"], received_json_data["count"]]):

           result.append({"price": row.price})
        json_data = json.dumps(result, cls=DjangoJSONEncoder)
        json_data1 = jsonpickle.decode(json_data)
        return HttpResponse(json_data1, content_type="application/json")
