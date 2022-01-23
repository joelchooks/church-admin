from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from member_app.models import Message

from member_app.models import Member, MemberAttendance, Service
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from crispy_forms.bootstrap import InlineField
from django.forms.widgets import NumberInput, DateInput, SelectDateWidget, Textarea


class SMSForm(forms.ModelForm):
    class Meta():
        model = Message
        fields = ('sender_name','recipients','message_text','flash')

        widgets = {
            'sender_name':forms.TextInput(attrs={'id':'sendName', }),
            'recipients':forms.Textarea(attrs={'rows':4, 'cols':200, 'id':'sendRecipe', }),
            'message_text':forms.Textarea(attrs={'rows':6, 'cols':200, 'id':'sendMess', }),
            'flash':forms.Select(attrs={'id':'sendFlas'})
        }

        labels = {
            'sender_name': 'Sender Name',
            'recipients': 'Recipient(s)',
            'message_text': 'Message Body',
            'flash': 'Flash Message?'
        }