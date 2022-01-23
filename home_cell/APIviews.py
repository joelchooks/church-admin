# Create your views here.
from django.http.response import JsonResponse
from member_app.models import HomeCell
from rest_framework.decorators import api_view, APIView, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.




# search view

class CellSearchView(APIView):
    def get(self, *args, **kwargs):
        query = kwargs["q"]
    
        result = HomeCell.objects.filter(Q(cell_name__icontains=query) | Q(cell_leader__icontains=query) | Q(
            cell_address__icontains=query)).all()
        resulter = list(result.values())
        return JsonResponse({'filt_data':resulter}, status=status.HTTP_200_OK, safe=False)



class CellJsonView(ListView):
    def get(self, *args, **kwargs):
        # print (kwargs)
        cells = list(HomeCell.objects.values())
        return JsonResponse({'cell_data':cells,}, safe=False)

