from django.db.models import fields
from rest_framework.serializers import *
from api.models import *

class ser_transport(ModelSerializer):
    class Meta:
        model = transport
        fields = '__all__'

class ser_number_of_day(ModelSerializer):
    class Meta:
        model = number_of_day
        fields = '__all__'

class ser_number_of_trip(ModelSerializer):
    class Meta:
        model = number_of_trip
        fields = '__all__'

class ser_tarif(ModelSerializer):
    transports = ser_transport(read_only=True, many=True)
    # number_of_day_id = ser_number_of_day()

    class Meta:
        model = tarif
        fields = '__all__'

class ser_card(ModelSerializer):
    class Meta:
        model = card
        fields = '__all__'

class ser_transaction(ModelSerializer):
    tarif_id = ser_tarif() 

    class Meta:
        model = transaction
        fields = '__all__'