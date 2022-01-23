from operator import mod
from django.db import models
from django.db.models.fields import BigIntegerField
from phone_field import PhoneField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.urls import reverse
from birthday import BirthdayField, BirthdayManager
from datetime import date, datetime

# Create your models here.

class Lyrics(models.Model):

    Year_Choices = zip(range(1950, 2023), range(1950, 2023))

    category_choices = (
        ('Praise Song', 'Praise Song'),
        ('Worship Song', 'Worship Song'),
        ('Christmas Song', 'Christmas Song'),
        ('Dr. Paul Song', 'Dr. Paul Song'),
        ('Hymn', 'Hymn')
    )

    lyrics_id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=50,)
    song_lyrics = models.TextField()
    artist = models.CharField(max_length=50, help_text="Type 'Unkwown' if Artist name is unkwown")
    album = models.CharField(max_length=50, blank=True)
    year_recorded = models.IntegerField(choices=Year_Choices, default=2021, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(default=datetime.now, editable=False)
    category = models.CharField(max_length=50, choices=category_choices, default='Praise Song')

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.song_name

    def get_absolute_url(self):
        return reverse('lyrics_app:detail', kwargs={'pk': self.pk})

    def capitalize(self):
        return self.song_name.title()
    
    def save(self, *args, **kwargs):
        self.song_name = self.song_name.title()
        self.last_updated = datetime.now()
        super(Lyrics, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.song_lyrics = self.song_lyrics.replace("\n", " ").replace("\r", " ")
    #     super(Lyrics, self).save(*args, **kwargs)

    