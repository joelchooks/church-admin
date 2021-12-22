from rest_framework import serializers
from member_app.models import Member
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
# Model Serializer


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('member_id', 'first_name', 'middle_name', 'last_name', 'gender', 'state_of_origin', 'address', 'date_joined','department', 'phone_number', 'email', 'home_cell', 'marital_status', 'occupation', 'wing', 'birthday')
