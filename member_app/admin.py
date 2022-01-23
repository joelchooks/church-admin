from django.contrib import admin

from .models import HomeCell, Message, Service
from .models import Member, MemberAttendance
# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    search_fields = ['member_id', 'first_name', 'middle_name', 'last_name', 'gender', 'state_of_origin', 'address', 'date_joined',
                     'birth_day', 'birth_month', 'department', 'phone_number', 'email', 'home_cell', 'marital_status', 'occupation']


admin.site.register(Member, MemberAdmin),
admin.site.register(HomeCell)

class ServiceInline(admin.TabularInline):
    model = Service
    fields = ['no_of_men', 'no_of_women', 'no_of_children', 'no_of_new_comers', 'no_of_new_converts', 'total']
    extra = 1

@admin.register(MemberAttendance)
class MemberAttendanceAdmin(admin.ModelAdmin):
     inlines = [
        ServiceInline
    ]

admin.site.register(Message)
 
    
