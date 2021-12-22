from django.db import models
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from member_app.forms import MemberForm
from member_app.models import Member
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
import json
from datetime import date, datetime

# Create your views here.


def index(request):
    return render(request, 'index.html')

    # members = Member.objects.all()
    # context = {
    #    'members': members
    # }
    # return render(request, 'index.html', context=context)


class MemberListView(ListView):
    model = Member
    template_name = 'church_app/member_list.html'
    context_object_name = 'members'

    def get_queryset(self):
        return Member.objects.filter(date_joined__lte=timezone.now()).order_by('date_joined')

    def defaultconverter(self, o):
        if isinstance(o, (datetime, date)):
            return o.__str__()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(
            list(Member.objects.values()), default=self.defaultconverter)
        return context


def MemberDetailView(request, pk):
    member = Member.objects.get(pk=pk)
    context = {
        'member': member
    }
    return render(request, 'church_app/member_detail.html', context=context)


def MemberFormView(request):
    form = MemberForm()

    if request.method == "POST":
        form = MemberForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/members')

        else:
            print('ERROR! Form is Invalid')

    return render(request, 'church_app/member_formpage.html', {'form': form})


class MemberUpdateView(UpdateView):
    template_name = 'church_app/member_formpage.html'
    model = Member
    redirect_field_name = 'church_app/member_detail.html'
    form_class = MemberForm


def MemberDeleteView(request, pk):
    member = Member.objects.get(pk=pk)
    member.delete()

    return redirect('/members')
    # return redirect('MemberDetailView', pk=pk)


# class MemberDeleteView(DeleteView):
#     template_name = 'church_app/member_formpage.html'
#     model = Member
#     success_url = reverse_lazy ('church_app:list')


# class MemberDetailView(DetailView):
#     model = Member
#     template_name = 'index.html'
