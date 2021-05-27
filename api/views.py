from django.shortcuts import render
from api.serialization import *
from api.models import *
from rest_framework import generics
from rest_framework.decorators import api_view

# Create your views here.

class CardView(generics.ListAPIView):
    queryset = card.objects.all()
    serializer_class = ser_card

class CardByNameView(generics.ListAPIView):
    serializer_class = ser_card

    # def get_queryset(request, card_number=None):
    #     cards = card.object.get(number=number)
    #     card_number = request.GET('card_number')

    def get_queryset(self):
        # print(self.kwargs['card_number'])
        # print(card.objects.filter(number=self.kwargs['card_number']).distinct())
        return card.objects.filter(number=self.kwargs['card_number']).distinct()

class TransportView(generics.ListAPIView):
    queryset = transport.objects.all()
    serializer_class = ser_transport

class TransportIdView(generics.RetrieveAPIView):
    queryset = transport.objects.all().order_by('name')
    serializer_class = ser_transport

class TransactionView(generics.ListAPIView):
    queryset = transaction.objects.all()
    serializer_class = ser_transaction

class TransactionViewID(generics.ListAPIView):
    # queryset = transaction.objects.all()
    serializer_class = ser_transaction

    def get_queryset(self):
        # print(self.kwargs['card_number'])
        # print(card.objects.filter(number=self.kwargs['card_number']).distinct())
        return transaction.objects.filter(card_id=self.kwargs['card']).distinct()

    