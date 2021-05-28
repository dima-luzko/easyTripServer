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

class ser_transport_tarif(ModelSerializer):
    transport_id = ser_transport()
    tarif_id = ser_tarif()
    
    class Meta:
        model = transport_tarif
        fields = '__all__'

class change_transport_tarif(RelatedField):

    def get_queryset(self):
        return ser_transport_tarif.filter(trans=self.kwargs['transport_id']).distinct()
        
     



class ser_transaction(ModelSerializer):
    tarif_id = ser_tarif() 
    transport_tarif = ser_transport_tarif(read_only=True, many=True)

    class Meta:
        model = transaction
        fields = '__all__'

# class ser_transaction(ModelSerializer):
#     tarif_id = change_transport_tarif(read_only=True, many=True)
#     #transport_tarif = change_transport_tarif(read_only=True, many=True)
    

#     class Meta:
#         model = transaction
#         fields = ['tarif_id']

    