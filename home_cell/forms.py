from django import forms
from django.forms import widgets

from member_app.models import HomeCell

class CellForm(forms.ModelForm):
    class Meta:
        model = HomeCell
        fields = '__all__'
        exclude = ('last_updated',)

        widgets = {
            'cell_name': forms.TextInput(),
            'cell_leader': forms.Select(),
            'cell_address': forms.TextInput(),
            'is_active': forms.Select()

        }

        labels = {
            'cell_name': 'Home Cell Name',
            'cell_leader': 'Cell Leader',
            'cell_address': 'Address',
            'is_active': 'Is Cell Active?'
        }

    
