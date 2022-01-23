
import birthday
import django_filters
from .models import *
from django.forms.widgets import DateInput, SelectDateWidget

class OrderMemberFilter(django_filters.FilterSet):
    date_joined = django_filters.DateFilter(
        field_name= 'date_joined',
        label= 'Specify Date',
        widget=DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        )
    )
    date_joined__gt = django_filters.DateFilter(
        field_name="date_joined",
        label= 'Date From',
        lookup_expr='gte',
        widget=DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        )
    )
    date_joined__lt = django_filters.DateFilter(
        field_name= "date_joined",
        label= 'Date To',
        lookup_expr='lte',
        widget=DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        )
    ) 

    birthday__gte = django_filters.DateFilter(
        field_name="birthday",
        label= 'Birthday From',
        lookup_expr='gte',
        widget=DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        )
    )
    birthday__lte = django_filters.DateFilter(
        field_name= "birthday",
        label= 'Birthday To',
            lookup_expr='lte',
            widget=DateInput(
                attrs={
                    'id': 'datepicker',
                    'type': 'date'
                }
            )
        ) 
     
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'phone_number', 'department', 'phone_number', 'home_cell', 'wing', 'gender', 'is_member']

        labels = {
            'gender': 'GENDER',
            'birth_day': 'BIRTH DAY',
            'department': 'DEPARTMENT',
            'phone_number': 'PHONE NUMBER',
            'home_cell':'HOME CELL',
            'wing':'WING',
            }