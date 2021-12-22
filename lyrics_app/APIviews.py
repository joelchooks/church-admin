from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Lyrics
from .serializers import LyricsSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, APIView, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
# Create your views here.


# search view

class LyricsSearchView(APIView):
    def get(self, *args, **kwargs):
        query = kwargs["q"]
        result = Lyrics.objects.filter(Q(song_name__icontains=query) | Q(song_lyrics__icontains=query) | Q(
            artist__icontains=query) | Q(album__icontains=query) | Q(
            category__icontains=query)).all()
        print(result)
        result = LyricsSerializer(result, many=True)
        return Response(result.data, status=status.HTTP_200_OK)


class LyricsList(generics.ListCreateAPIView):
    queryset = Lyrics.objects.all()
    serializer_class = LyricsSerializer


class LyricsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lyrics.objects.all()
    serializer_class = LyricsSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)
