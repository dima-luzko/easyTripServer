from django.db import connection
from django.shortcuts import render
from api.serialization import *
from api.models import *
from rest_framework import generics
from rest_framework.decorators import api_view
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
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

# должно быть если number_of_day_id : 5 , transports: 1 , count: 1; price = 11.88
# json: {
#     "price": null,
#     "number_of_day_id": 5,
#     "number_of_trip_id": null,
#     "transports": 1,
#     "count": 1
# }
@csrf_exempt
def NumberOfDaysTarif1(request):
     if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        result = []
        for row in tarif.objects.raw('''
        SELECT * FROM api_tarif 
        INNER JOIN api_tarif_transports ON api_tarif.id = api_tarif_transports.tarif_id 
        INNER JOIN api_transport ON api_tarif_transports.transport_id = api_transport.id 
        WHERE api_tarif.number_of_day_id_id = %s
        AND api_transport.id in (%s)
        AND api_tarif.id
        NOT IN (SELECT tarif_id FROM api_tarif_transports WHERE transport_id NOT IN (%s))
        GROUP BY api_tarif.id
        HAVING COUNT(*) = %s
        ''', [received_json_data["number_of_day_id"],received_json_data["transports"], received_json_data["transports"], received_json_data["count"]]):

           result.append({"price": row.price, "number_of_day_id": row.number_of_day_id, "transports": row.transports})
        json_data = json.dumps(result, cls=DjangoJSONEncoder)

        return HttpResponse(json_data, content_type="application/json")

@csrf_exempt
def NumberOfDaysTarif(request):
     if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        result = []
        for row in tarif.objects.raw('''
        SELECT * FROM api_tarif 
        INNER JOIN api_tarif_transports ON api_tarif.id = api_tarif_transports.tarif_id 
        INNER JOIN api_transport ON api_tarif_transports.transport_id = api_transport.id 
        WHERE api_tarif.number_of_day_id_id = %s
        ''', [received_json_data["number_of_day_id"]]):

           result.append({"price": row.price, "number_of_day_id": row.number_of_day_id, "transports": row.transports})
        json_data = json.dumps(result, cls=DjangoJSONEncoder)

        return HttpResponse(json_data, content_type="application/json")
        
        #  print({"price" :result})



# class NumberOfDaysTarifView(generics.CreateAPIView):
#     serializer_class = ser_tarif

#     def post(self, request, *args, **kwargs):
#         received_json_data = json.loads(request.body.decode("utf-8"))
#         # queryset1 = transport.objects.filter(id__in=)
#         queryset = tarif.objects.filter(number_of_day_id=received_json_data["number_of_day_id"]).filter(transports=received_json_data["transport"])
#         data = [entry for entry in queryset.values()]
#         json_data = json.dumps(data)

#         return HttpResponse(json_data, content_type="application/json")


# select tf.price from api_tarif tf
# inner join api_tarif_transports tt on tf.id = tt.tarif_id    - select_related
# inner join api_transport tp on tt.transport_id = tp.id
# where tf.number_of_day_id_id = 5
# and tp.id in (1,2,6)
# and tf.id not in (select tarif_id from api_tarif_transports where transport_id not in (1,2,6))
# group by tf.id
# having count(*) = 3;
