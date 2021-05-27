from django.db import models

# Create your models here.
class transport(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class number_of_day(models.Model):
    value = models.IntegerField(null=True,blank=True)

    def __int__(self):
        return self.value

class number_of_trip(models.Model):
    value = models.IntegerField(null=True,blank=True)

    def __int__(self):
        return self.value

class tarif(models.Model):
    number_of_day_id = models.ForeignKey(number_of_day,  blank=True, null=True, on_delete=models.SET_NULL)
    number_of_trip_id = models.ForeignKey(number_of_trip,  blank=True, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __decimal__(self):
        return self.price


class card(models.Model):
    number = models.CharField(max_length=17)

    def __str__(self):
        return self.number

class transaction(models.Model):
    card_id = models.ForeignKey(card, on_delete=models.CASCADE)
    tarif_id = models.ForeignKey(tarif, on_delete=models.CASCADE)
    start_data = models.DateField(null=True,blank=True)
    finish_data = models.DateField(null=True,blank=True)
    number_of_trip_left = models.IntegerField(null=True,blank=True)

    def __int__(self):
        return self.number_of_trip_left

class transport_tarif(models.Model):
    transport_id = models.ManyToManyField(transport)
    tarif_id = models.ManyToManyField(tarif)