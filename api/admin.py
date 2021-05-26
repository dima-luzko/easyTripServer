from django.contrib import admin
from api.models import *

# Register your models here.
@admin.register(transport)
class admin_transport(admin.ModelAdmin):
    list_display = ("id","name")
    ordering = ['id']

@admin.register(number_of_day)
class admin_number_of_day(admin.ModelAdmin):
    list_display = ("id","value")
    ordering = ['id']

@admin.register(number_of_trip)
class admin_number_of_trip(admin.ModelAdmin):
    list_display = ("id","value")
    ordering = ['id']

@admin.register(tarif)
class admin_tarif(admin.ModelAdmin):
    list_display = ("id","number_of_day_id","number_of_trip_id","price")
    ordering = ['id']

@admin.register(card)
class admin_card(admin.ModelAdmin):
    list_display = ("id","number")
    ordering = ['id']

@admin.register(transaction)
class admin_transaction(admin.ModelAdmin):
    list_display = ("id","card_id","tarif_id","start_data","finish_data","number_of_trip_left")
    ordering = ['id']

@admin.register(transport_tarif)
class admin_transport_tarif(admin.ModelAdmin):
    ordering = ['transport_id']