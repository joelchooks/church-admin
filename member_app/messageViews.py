from django.db import models
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.views.generic.detail import SingleObjectMixin
from member_app.models import Message
from django.conf import settings
from member_app.messageForms import SMSForm
from member_app.models import Member, MemberAttendance, Service
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView, FormView
from django.urls import reverse_lazy, reverse
from django.utils import timezone
import json
from datetime import date, datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect



class MessageListView(LoginRequiredMixin, ListView):
    template_name = 'messages/message_list.html'
    model = Message
    context_object_name = 'objects'

    def get_queryset(self):
        return Message.objects.filter(approved_message=True).order_by('-sent_date')
    


@login_required
def MessageFormView(request):
    form = SMSForm()

    if request.method == 'POST':
        form = SMSForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('church_app:message_draft')
    else:
            form = SMSForm()
    return render(request, 'messages/message_formpage.html', {'form':form})


@login_required
def MessageDetailView(request, pk):
    object = get_object_or_404(Message, pk=pk)
    return render(request, 'messages/message_detail.html', {'object':object})


class MessageDraftView(LoginRequiredMixin, ListView):
    template_name = 'messages/message_draft.html'
    login_url = '/login/'
    model = Message
    context_object_name = 'objects'
    # redirect_field_name = 'post_draft_list.html'

    def get_queryset(self):
        return Message.objects.filter(approved_message=False).order_by('-created_date')


class UpdateMessageView(LoginRequiredMixin, UpdateView):
    template_name = 'messages/message_formpage.html'
    login_url = '/login/'
    model = Message
    form_class = SMSForm

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("church_app:draft_message_detail", kwargs={"pk": pk})


@login_required
def DraftMessageDetailView(request, pk):
    object = get_object_or_404(Message, pk=pk)
    return render(request, 'messages/message_draft_detail.html', {'object':object, 'api_key':settings.BULK_SMS_API_KEY, 'username':settings.BULK_SMS_USERNAME})


# @login_required
# def SuccessMessage(request, pk):
#     if request.is_ajax:
#         object = get_object_or_404(Message, pk=pk)
#         object.approve()
#         result['success'] = 'successful!'
#         else: 
#             result['error'] = 'failed!'
#         return HttpResponse(
#             json.dumps(result),
#             content_type="application/json"
#         )
#     else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )
   
    # return render(request, 'messages/message_success_detail.html')
