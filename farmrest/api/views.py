from rest_framework import generics, permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import FarmDataSerializer
from .models import FarmData
# Create your views here.


class TotalGpsMessagesView(generics.ListAPIView):
    """API Get to acquire Total GPS Messages"""
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        gps_count = FarmData.objects.exclude(gps_id=0).count()
        can_count = FarmData.objects.exclude(message_id='').count()
        content = {'gps_message_count': gps_count, 'can_message_count': can_count}
        return Response(content)

        #queryset = FarmData.objects.exclude(gps_id=0).count()
    #queryset = FarmData.objects.raw('SELECT COUNT(id) from api_farmdata where gps_id != ""')
    #serializer_class = FarmDataSerializer


class TotalUniqueMessages(generics.ListAPIView):
    """API Get to acquire total Unique messages namely CAN messages"""
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        unique_messages = FarmData.objects.exclude(message_id='').distinct().count()
        content = {'unique_can_messages': unique_messages}
        return Response(content)

