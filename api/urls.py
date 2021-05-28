from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [

    url(r'^cards/(?P<card_number>.+)/$', CardByNameView.as_view(), name='card_number'),
    url(r'^transactions_of_card/(?P<card>.+)/$', TransactionsOfCardView.as_view(), name='transactions_of_card_id'),
    url(r'^transports/$', TransportView.as_view(), name='transports'),
    url(r'^transports/(?P<pk>[0-9]+)/?$', TransportIdView.as_view(), name='transports_id'),
    url(r'^number_of_days/$', NumberOfDaysView.as_view(), name='number_of_days'),
    url(r'^number_of_trips/$', NumberOfTripsView.as_view(), name='number_of_trips'),

    url(r'^number_of_days_tarif/(?P<number_of_day_id>.+)/$', NumberOfDayIDView.as_view(), name='number_of_day_id'),
]
   

urlpatterns = format_suffix_patterns(urlpatterns)
