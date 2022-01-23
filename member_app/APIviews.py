import re
from django.http import response
from django.shortcuts import render
from django.http import Http404

# Create your views here.
from django.contrib.auth.models import User
from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Member, Message
from .serializers import MemberSerializer, MessageSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, APIView, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.


def index(request):
    return HttpResponse('You are welcome')

# search view

class MemberJsonView(LoginRequiredMixin, ListView):
    def get(self, *args, **kwargs):
        # print (kwargs)
        upper = kwargs.get('num_members')
        lower = upper - 15
        members = list(Member.objects.values()[lower:upper])
        members_size = len(Member.objects.all())
        size = True if upper >= members_size else False
        return JsonResponse({'memb_data':members, 'max_member':size}, safe=False)


# class MemberSearchView(APIView):
#     def get(self, *args, **kwargs):
#         query = kwargs["q"]
#         result = Member.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(
#             middle_name__icontains=query)).all()
#         # print(result)
#         result = MemberSerializer(result, many=True)
#         print(result.data)
#         return Response(result.data, status=status.HTTP_200_OK)



class MemberSearchView(APIView):
    def get(self, *args, **kwargs):
        query = kwargs["q"]
    
        result = Member.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(
            middle_name__icontains=query)).all()
        resulter = list(result.values())
        return JsonResponse({'filt_data':resulter}, status=status.HTTP_200_OK, safe=False)



class MessageAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)

# MESSAGES
class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# # Creat user viewset class
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
