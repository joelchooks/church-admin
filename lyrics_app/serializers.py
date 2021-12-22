from rest_framework import serializers
from lyrics_app.models import Lyrics
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
# Model Serializer


class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = '__all__'