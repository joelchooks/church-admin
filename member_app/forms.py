from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets

from member_app.models import Member, MemberAttendance, Service
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from crispy_forms.bootstrap import InlineField
from django.forms.widgets import NumberInput, DateInput, SelectDateWidget
# from bootstrap_datepicker_plus import DatePickerInput
from django.core.validators import RegexValidator, MinLengthValidator


class MemberForm(forms.ModelForm):
    class Meta():
        model = Member
        fields = '__all__'
        exclude = ('member_id', 'is_member', 'member_age',)

        widgets = {
            'first_name': forms.TextInput(),
            'middle_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'gender': forms.Select(),
            'phone_number': forms.TextInput(attrs={'placeholder':"Enter Numbers Only", 'type': 'tel',}),
            'other_number': forms.TextInput(attrs={'placeholder':"Enter Numbers Only", 'type': 'tel',}),
            'email': forms.EmailField(),
            'state_of_origin': forms.Select(),
            'address': forms.TextInput(),
            'department': forms.Select(),
            'email': forms.EmailInput(),
            'home_cell': forms.Select(),
            'marital_status': forms.Select(),
            'occupation': forms.TextInput(),
            'wing': forms.Select(attrs={'placeholder':"E.g: Men's Forum"}),
            'member_status': forms.Select(),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'is_baptized': forms.Select(),
            'done_foundation': forms.Select(),
            'done_maturity':forms.Select(),
        }

        labels = {
            'first_name': 'First Name',
            'middle_name': 'Middle Name',
            'last_name': 'Last Name',
            'gender': 'Gender',
            'phone_number': 'Phone Number',
            'other_number': 'Other Number',
            'email':'E-mail',
            'state_of_origin': 'State Of Origin',
            'address': 'House Address',
            'department': 'Department',
            'home_cell':'Home Cell',
            'marital_status': 'Marital Status',
            'occupation':'Occupation',
            'wing':'Forum',
            'member_status':'Member Status', 
            'birthday': 'Birthday',
            'is_baptized':'Water Baptism Status',
            'done_foundation':'Done Foundation Class?',
            'done_maturity':'Done Maturity Class?'       
            }




class MemberAttendanceForm(forms.ModelForm):
    class Meta:
        model = MemberAttendance
        fields = ('date', 'service_Type',)

        widgets = {
            'date': forms.SelectDateWidget(attrs = {'type': 'date'})
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'



# DatePickerInput(
#                 options={
#                     "format": "mm/dd/yyyy",
#                     "autoclose": True})

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'POST'
    #     self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))

    #     self.helper.layout = Layout(
    #         InlineField(
    #             Column('first_name'),
    #             Column('middle_name')
    #         )
    #     )

