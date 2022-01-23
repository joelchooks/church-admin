from django.db import models
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from lyrics_app.forms import LyricsForm
from lyrics_app.models import Lyrics
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.utils import timezone
import json
from datetime import date, datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

# List View
class LyricsListView(ListView):
    queryset = Lyrics.objects.all()
    template_name = 'lyrics_app/lyrics_list.html'
    context_object_name = 'lyrics'

    # def get_queryset(self):
    #     return Lyrics.objects.filter(date_added__lte=timezone.now()).order_by('-date_added')

    def defaultconverter(self, o):
        if isinstance(o, (datetime, date)):
            return o.__str__()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(
            list(Lyrics.objects.values()), default=self.defaultconverter)
        return context


# Detail View
def LyricsDetailView(request, pk):
    lyric = Lyrics.objects.get(pk=pk)
    context = {
        'lyric': lyric
    }
    return render(request, 'lyrics_app/lyrics_detail.html', context=context)


# FormView
class LyricsFormView(CreateView):
    queryset = Lyrics.objects.all()
    template_name = 'lyrics_app/lyrics_formpage.html'
    form_class = LyricsForm

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Song Lyrics Added Successfully'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form is invalid')
        messages.add_message(
            self.request,
            messages.ERROR,
            'Error!'
        )
        return self.render_to_response({'form':form})




# def LyricsFormView(request):
#     form = LyricsForm()

#     if request.method == "POST":
#         form = LyricsForm(request.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('/lyrics')

#         else:
#             print('ERROR! Form is Invalid')

#     return render(request, 'lyrics_app/lyrics_formpage.html', {'form': form})



# Update View
class LyricsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'lyrics_app/lyrics_formpage.html'
    model = Lyrics
    form_class = LyricsForm

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Song Lyrics Updated Successfully'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form is invalid')
        messages.add_message(
            self.request,
            messages.ERROR,
            'Error!'
        )
        return self.render_to_response({'form':form})



@login_required
def LyricsDeleteView(request, pk):
    member = Lyrics.objects.get(pk=pk)
    member.delete()
    messages.success(request, 'Lyric Successfuly Deleted.')
    return redirect('/lyrics')
    # return redirect('MemberDetailView', pk=pk)



# class LyricsConfirmDeleteView(LoginRequiredMixin, DeleteView):
#     template_name = 'lyrics_app/lyrics_confirm_delete.html'
#     model = Lyrics
#     success_url = reverse_lazy('lyrics_app:list')

