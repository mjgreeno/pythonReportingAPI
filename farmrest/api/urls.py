from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TotalGpsMessagesView
from .views import TotalUniqueMessages

urlpatterns = {
    url(r'^totalgps/$', TotalGpsMessagesView.as_view(), name="Total GPS Messages"),
    url(r'^totaluniquecan/$', TotalUniqueMessages.as_view(), name="Total Unique CAN Messages"),
}

urlpatterns = format_suffix_patterns(urlpatterns)