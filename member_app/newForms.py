from django.forms.models import inlineformset_factory

from .models import MemberAttendance, Service

MemberAttendanceServiceFormset = inlineformset_factory(MemberAttendance, Service, fields=('no_of_men', 'no_of_women', 'no_of_children', 'no_of_new_comers', 'no_of_new_converts', 'total'))