from django.contrib import admin
from member_app.models import Member
# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    search_fields = ['member_id', 'first_name', 'middle_name', 'last_name', 'gender', 'state_of_origin', 'address', 'date_joined',
                     'birth_day', 'birth_month', 'department', 'phone_number', 'email', 'home_cell', 'marital_status', 'occupation']


admin.site.register(Member, MemberAdmin)
