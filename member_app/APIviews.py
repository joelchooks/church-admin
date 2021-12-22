from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Member
from .serializers import MemberSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, APIView, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
# Create your views here.


def index(request):
    return HttpResponse('You are welcome')

# search view


class MemberSearchView(APIView):
    def get(self, *args, **kwargs):
        query = kwargs["q"]

        result = Member.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(
            middle_name__icontains=query)).all()
        # print(result)
        result = MemberSerializer(result, many=True)
        return Response(result.data, status=status.HTTP_200_OK)


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)


# # Creat user viewset class
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
