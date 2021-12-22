from django.db import models
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from lyrics_app.forms import LyricsForm
from lyrics_app.models import Lyrics
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
import json
from datetime import date, datetime

# Create your views here.

class LyricsListView(ListView):
    model = Lyrics
    template_name = 'lyrics_app/lyrics_list.html'
    context_object_name = 'lyrics'

    def get_queryset(self):
        return Lyrics.objects.filter(date_added__lte=timezone.now()).order_by('-date_added')

    def defaultconverter(self, o):
        if isinstance(o, (datetime, date)):
            return o.__str__()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(
            list(Lyrics.objects.values()), default=self.defaultconverter)
        return context


def LyricsDetailView(request, pk):
    lyric = Lyrics.objects.get(pk=pk)
    context = {
        'lyric': lyric
    }
    return render(request, 'lyrics_app/lyrics_detail.html', context=context)


def LyricsFormView(request):
    form = LyricsForm()

    if request.method == "POST":
        form = LyricsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/lyrics')

        else:
            print('ERROR! Form is Invalid')

    return render(request, 'lyrics_app/lyrics_formpage.html', {'form': form})


class LyricsUpdateView(UpdateView):
    template_name = 'lyrics_app/lyrics_formpage.html'
    model = Lyrics
    redirect_field_name = 'lyrics_app/lyrics_detail.html'
    form_class = LyricsForm


def LyricsDeleteView(request, pk):
    lyric = Lyrics.objects.get(pk=pk)
    lyric.delete()

    return redirect('/lyrics')