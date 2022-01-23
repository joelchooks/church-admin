# Create your views here.

from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, APIView
from django.db.models import Q
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from datetime import date, timezone, datetime
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from member_app.models import Member
from member_app.models import HomeCell
from .forms import CellForm



# API VIEWS
class CellSearchView(APIView):
    def get(self, *args, **kwargs):
        query = kwargs["q"]
    
        result = HomeCell.objects.filter(Q(cell_name__icontains=query) | Q(
            cell_address__icontains=query)).all()
        resulter = list(result.values())
        return JsonResponse({'filt_data':resulter}, status=status.HTTP_200_OK, safe=False)



class CellJsonView(ListView):
    def get(self, *args, **kwargs):
        # print (kwargs)
        cells = list(HomeCell.objects.values())
        return JsonResponse({'cell_data':cells,}, safe=False)



# List View
class CellListView(ListView):
    queryset = HomeCell.objects.all()
    template_name = 'home_cell/cell_list.html'
    extra_context = {'cells':queryset}
    # paginate_by = 30

    # def get_queryset(self):
    #     return Member.objects.filter(date_joined__lte=timezone.now()).order_by('date_joined')
     

    def defaultconverter(self, o):
        if isinstance(o, (datetime, date)):
            return o.__str__()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(
            list(HomeCell.objects.values()), default=self.defaultconverter)
        return context

    
# Detail View
@login_required
def CellDetailView(request, pk):
    cell = HomeCell.objects.get(pk=pk)
	
    context = {
        'cell': cell,
    }

    return render(request, 'home_cell/cell_detail.html', context=context)


# Form View
class CellFormView(CreateView):
    template_name = 'home_cell/cell_form.html'
    queryset = HomeCell.objects.all()
    form_class = CellForm

    def get_success_url(self):
        return reverse('home_cell:cell_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'New Cell Successfuly Added.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        print ("form is invalid")
        messages.add_message(
            self.request,
            messages.ERROR,
            'Error!'
        )
        return self.render_to_response({
            'form': form,})
    

class CellUpdateView(UpdateView):
    template_name = 'home_cell/cell_form.html'
    model = HomeCell
    form_class = CellForm

    def get_success_url(self):
        return reverse('home_cell:cell_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes Successfuly Saved.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        print ("form is invalid")
        messages.add_message(
            self.request,
            messages.ERROR,
            'Error!'
        )

        return self.render_to_response({
            'form': form,})
    
@login_required
def CellDeleteView(request, pk):
	cell = HomeCell.objects.get(pk=pk)
	cell.delete()
	messages.success(request, 'Cell Successfuly Deleted.')
	return redirect('/homecell')
