from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TotalGpsMessagesView
from .views import TotalUniqueMessages
from .views import TimeBetweenTimeStamps
from .views import AverageMessages
from .views import MostCanMessages


urlpatterns = {
    url(r'^totalgps/$', TotalGpsMessagesView.as_view(), name="Total GPS Messages"),
    url(r'^totaluniquecan/$', TotalUniqueMessages.as_view(), name="Total Unique CAN Messages"),
    url(r'^timebetweendates/$', TimeBetweenTimeStamps.as_view(), name="Total Time of Dataset"),
    url(r'^avgmessages/$', AverageMessages.as_view(), name="Average CAN and GPS Messages per second"),
    url(r'^mostcanmessages/$', MostCanMessages.as_view(), name="Most CAN messages from timestamp"),
}

urlpatterns = format_suffix_patterns(urlpatterns)


