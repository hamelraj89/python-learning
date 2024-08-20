from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(requests):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(requests):
    rooms = Room.objects.all()
    roomssssss = RoomSerializer(rooms, many=True)
    return Response(roomssssss.data)