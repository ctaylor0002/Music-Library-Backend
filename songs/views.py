from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import SongSerializer
from .models import Song
from songs import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def songs_list(request):

    if request.method == 'GET':

        songs = Song.objects.all()

        song_serializer = SongSerializer(songs, many=True)
        return Response(song_serializer.data)

    elif request.method == 'POST':
        song_serializer = SongSerializer(data=request.data)
        song_serializer.is_valid(raise_exception=True)
        song_serializer.save()  
        return Response(song_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def songs_details(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serialized_data = SongSerializer(song)
        return Response(serialized_data.data)

    elif request.method == 'PUT':
        serialized_data = SongSerializer(song, data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PATCH':
        song = get_object_or_404(Song, pk=pk)

        song.likes = (song.likes) + 1
        
        song.save()
        serialized_data = SongSerializer(song)
    
        return Response(serialized_data.data, status=status.HTTP_200_OK)

