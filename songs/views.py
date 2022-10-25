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


@api_view(['GET', 'PUT', 'DELETE'])
def songs_details(request, pk):
    song = get_object_or_404(Songs, pk=pk)
    if request.method == 'GET':
        serialized_data = SongsSerializer(song)
        return Response(serialized_data.data)

    elif request.method == 'PUT':
        serialized_data = SongsSerializer(song, data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)