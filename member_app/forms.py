from django import forms
from django.db.models import fields
from member_app.models import Member
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from crispy_forms.bootstrap import InlineField
from django.forms.widgets import NumberInput, DateInput, SelectDateWidget


class MemberForm(forms.ModelForm):
    class Meta():
        model = Member
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'myformcontent'}),
            'middle_name': forms.TextInput(attrs={'class': 'myformcontent'}),
            'last_name': forms.TextInput(attrs={'class': 'myformcontent'}),
            'gender': forms.Select(attrs={'class': 'myformcontent'}),
            'phone_number': forms.TextInput(attrs={'type': 'tel', 'class': 'myformcontent'}),
            'state_of_origin': forms.Select(attrs={'class': 'myformcontent'}),
            'address': forms.TextInput(attrs={'class': 'myformcontent'}),
            'department': forms.TextInput(attrs={'class': 'myformcontent'}),
            'email': forms.EmailInput(attrs={'class': 'myformcontent'}),
            'home_cell': forms.TextInput(attrs={'class': 'myformcontent'}),
            'marital_status': forms.Select(attrs={'class': 'myformcontent'}),
            'occupation': forms.TextInput(attrs={'class': 'myformcontent'}),
            'wing': forms.Select(attrs={'class': 'myformcontent'}),
            'birthday': forms.SelectDateWidget(empty_label=('Year', 'Month', 'Day'))
        }

        labels = {
            'first_name': 'FIRST NAME',
            'middle_name': 'MIDDLE NAME',
            'last_name': 'LAST NAME',
            'gender': 'GENDER',
            'state_of_origin': 'STATE OF ORIGIN',
            'address': 'ADDRESS',
            'birth_day': 'BIRTH DAY',
            'birth_month': 'BIRTH MONTH',
            'department': 'DEPARTMENT',
            'phone_number': 'PHONE NUMBER',
            'email':'EMAIL',
            'home_cell':'HOME CELL',
            'marital_status': 'MARITAL STATUS',
            'occupation':'OCCUPATION',
            'wing':'WING',
            'birthday':'BIRTHDATE'
            }

        

        

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
                
