from datetime import datetime
from django.db import models
from django.urls import reverse
from datetime import date, timezone, datetime

# Create your models here.

class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    note_title = models.CharField(max_length=50, blank=True)
    note_text = models.TextField(max_length=99999999,)
    date_added = models.DateTimeField(datetime.now, editable=False)
    last_updated = models.DateTimeField(editable=False)


    class Meta:
        ordering = ['-last_updated']

    def __str__(self):
        if self.note_title:
            return f'{self.note_title}'
        return f'{self.note_text[0:15]}...'

    # def get_absolute_url(self):
    #     return reverse('notes_app:detail', kwargs={'pk': self.pk})
    
    
    def save(self, *args, **kwargs):
        self.last_updated = datetime.now()
        super(Note, self).save(*args, **kwargs)

