from rest_framework import generics, permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import FarmData
from django.db import connection
from django.http import HttpResponse


class TotalGpsMessagesView(generics.ListAPIView):
    """API Get to acquire Total GPS Messages"""
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        gps_count = FarmData.objects.exclude(gps_id=0).count()
        can_count = FarmData.objects.exclude(message_id='').count()
        content = {'gps_message_count': gps_count, 'can_message_count': can_count}
        return Response(content)


class TotalUniqueMessages(generics.ListAPIView):
    """API Get to acquire total Unique messages namely CAN messages"""
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        unique_messages = FarmData.objects.exclude(message_id='').distinct().count()
        content = {'unique_can_messages': unique_messages}
        return Response(content)


class TimeBetweenTimeStamps(generics.ListAPIView):
    """API Get to acquire time between dates and date time operations"""
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):

        cursor = connection.cursor()
        cursor.execute(
            """SELECT (strftime('%s',max(ts)) - strftime('%s', min(ts))) As seconds FROM api_farmdata""")
        rows = cursor.fetchall()
        result = []
        keys = ('seconds',)
        for row in rows:
            result.append(dict(zip(keys, row)))
        json_data = json.dumps(result)
        return HttpResponse(json_data, content_type="application/json")


class AverageMessages(generics.ListAPIView):
    """API Get to acquire Average CAN messages per second of run time and per gps message"""
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):

        cursor = connection.cursor()
        cursor.execute(
            """SELECT (strftime('%s',max(ts)) - strftime('%s', min(ts))) / cast(count(message_id) as float) AS test FROM api_farmdata WHERE message_id != ''""")
        rows = cursor.fetchone()
        content = {'avg_can_messages': rows}
        return Response(content)


class MostCanMessages(generics.ListAPIView):
    """The first ts (timestamp) that contains the most CAN messages"""
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        cursor = connection.cursor()
        cursor.execute(
            """select ts, count(*) seconddata  from ( 
               select message_id, ts, count(*) seconddata FROM api_farmdata WHERE message_id != "" group by message_id, ts order by seconddata desc
               ) as a 
               group by ts
               order by seconddata desc
              limit 1""")
        rows = cursor.fetchone()
        content = {'most_can_messages': rows}
        return Response(content)


class LeastCanMessages(generics.ListAPIView):
    """The first ts (timestamp) that contains the least CAN messages"""
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        cursor = connection.cursor()
        cursor.execute(
            """select ts, count(*) seconddata  from ( 
               select message_id, ts, count(*) seconddata FROM api_farmdata WHERE message_id != "" group by message_id, ts order by seconddata asc
               ) as a 
               group by ts
               order by seconddata asc
              limit 1""")
        rows = cursor.fetchone()
        content = {'most_can_messages': rows}
        return Response(content)
