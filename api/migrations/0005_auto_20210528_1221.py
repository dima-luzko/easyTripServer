# Generated by Django 3.2.3 on 2021-05-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210526_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarif',
            name='transports',
            field=models.ManyToManyField(to='api.transport'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='number_of_trip_left',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='transport_tarif',
        ),
    ]
