from django import forms
from django.db import models
from django.db.models import fields
from lyrics_app.models import Lyrics
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from crispy_forms.bootstrap import InlineField
from django.forms.widgets import NumberInput, DateInput, SelectDateWidget


class LyricsForm(forms.ModelForm):
    class Meta:
        model = Lyrics
        fields = '__all__'

        widgets = {
            'song_name': forms.TextInput(),
            'song_lyrics': forms.Textarea(),
            'artist': forms.TextInput(),
            'album': forms.TextInput(),
            'year-recorded': forms.Select(),
            'category': forms.Select(),
        }

        labels = {
            'song_name': 'SONG NAME',
            'song_lyrics': 'LYRICS',
            'artist': 'ARTIST',
            'album': 'ALBUM',
            'year_recorded': 'YEAR RECORDED',
            'category': 'CATEGORY'
        }

        help_texts = {'artist': "Type 'Unkwown' if Artist name is unkwown",}


        