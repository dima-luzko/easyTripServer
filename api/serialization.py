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
    class Meta:
        model = tarif
        fields = '__all__'

class ser_card(ModelSerializer):
    class Meta:
        model = card
        fields = '__all__'

class ser_number_transaction(ModelSerializer):
    class Meta:
        model = transaction
        fields = '__all__'

class ser_transport_tarif(ModelSerializer):
    class Meta:
        model = transport_tarif
        fields = '__all__'