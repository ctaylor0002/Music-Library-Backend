from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import SongsSerializer
from .models import Songs
from songs import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def songs_list(request):

    if request.method == 'GET':

        songs = Songs.objects.all()

        song_serializer = SongsSerializer(songs, many=True)
        return Response(song_serializer.data)

    elif request.method == 'POST':
        song_serializer = SongsSerializer(data=request.data)
        song_serializer.is_valid(raise_exception=True)
        song_serializer.save()  
        return Response(song_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def songs_details(request, pk):
    song = get_object_or_404(Songs, pk=pk)
    if request.method == 'GET':
        serialized_data = SongsSerializer(song)
        return Response(serialized_data.data)

