from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import LikeSerializer
from .models import Likes
from likes import serializers
# from songs.models import Songs

# Create your views here.

@api_view(['POST'])
def music_like_condition(request, pk):
    type_param = request.query_params.get('like_condition')
    if request.method == 'POST':
        serializer = LikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        like_or_dislike_count = Likes.objects.filter(like_condition=(type_param)).count()
        return Response((serializer.data, f'This song has {like_or_dislike_count} {type_param}'), status=status.HTTP_201_CREATED)