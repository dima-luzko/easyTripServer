from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    url(r'^transactions/$', TransactionView.as_view(), name='transaction'),

    url(r'^transactions/(?P<card>.+)/$', TransactionViewID.as_view(), name='tcard_id'),

    url(r'^cards/(?P<card_number>.+)/$', CardByNameView.as_view(), name='card_number'),

    # url(r'^cards/$', CardView.as_view(), name='card'),
   
    url(r'^transports/$', TransportView.as_view(), name='transport'),
    url(r'^transports/(?P<pk>[0-9]+)/?$', TransportIdView.as_view(), name='transports_id'),
   
]
   

urlpatterns = format_suffix_patterns(urlpatterns)
