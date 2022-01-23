from django.db import models
from django.db.models import query
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.views.generic.detail import SingleObjectMixin
from member_app.serializers import MemberSerializer
from member_app.forms import MemberForm, MemberAttendanceForm, ServiceForm
from member_app.models import Member, MemberAttendance, Service
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView, FormView
from django.urls import reverse_lazy, reverse
from django.utils import timezone
import json
from datetime import date, datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from .filters import OrderMemberFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .newForms import MemberAttendanceServiceFormset

# Create your views here.

# Home View
def index(request):
    return render(request, 'index.html')


# Generate Member Details
@login_required
def GenerateMemberDetails(request):
    f = OrderMemberFilter(request.GET, queryset=Member.objects.all())

    paginated_f = Paginator(f.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginated_f.get_page(page_number)
    
    return render(request, 'church_app/generate_list/generate_member_list.html', {'filter': f, 'page_obj':page_obj})


# List View
class MemberListView(LoginRequiredMixin, ListView):
    queryset = Member.objects.all()
    template_name = 'church_app/member_list.html'
    extra_context = {'members':queryset, 'count':Member.objects.all().count()}
    # paginate_by = 30

    # def get_queryset(self):
    #     return Member.objects.filter(date_joined__lte=timezone.now()).order_by('date_joined')
     

    def defaultconverter(self, o):
        if isinstance(o, (datetime, date)):
            return o.__str__()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(
            list(Member.objects.values()), default=self.defaultconverter)
        
        return context

    
# Detail View
@login_required
def MemberDetailView(request, pk):
    member = Member.objects.get(pk=pk)
    gender = 'Male' if member.gender == 'Male' else 'Female'
    context = {
        'member': member,
        'gender': gender
    }

    return render(request, 'church_app/member_detail.html', context=context)


# Form View
class MemberFormView(LoginRequiredMixin, CreateView):
    template_name = 'church_app/member_formpage.html'
    queryset = Member.objects.all()
    # redirect_field_name = 'church_app/member_detail.html'
    form_class = MemberForm

    def get_success_url(self):
        return reverse('church_app:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'New Member Successfuly Added.'
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
    

class MemberUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'church_app/member_formpage.html'
    model = Member
    # redirect_field_name = 'church_app/member_detail.html'
    form_class = MemberForm

    def get_success_url(self):
        return reverse('church_app:detail', kwargs={'pk': self.object.pk})

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
    

# class MemberDeleteConfirm(LoginRequiredMixin, DeleteView):
#     template_name = 'church_app/member_confirm_delete.html'
#     model = Member
#     success_url = reverse_lazy('church_app:list')


@login_required
def MemberDeleteView(request, pk):
    member = Member.objects.get(pk=pk)
    member.delete()
    messages.success(request, 'Member Successfuly Deleted.')
    return redirect('/members')
    # return redirect('MemberDetailView', pk=pk)


class AttendanceListView(LoginRequiredMixin, ListView):
    model = MemberAttendance
    template_name = 'church_app/attendance/att_list.html'
    context_object_name = 'attend'

    
    def get_queryset(self):
        return MemberAttendance.objects.filter(date__lte=timezone.now()).order_by('-date')

    def defaultconverter(self, o):
        if isinstance(o, (datetime, date)):
            return o.__str__()

class AttendanceCreateView(LoginRequiredMixin, CreateView):
    model = MemberAttendance
    template_name = 'church_app/attendance/att_formpage.html'
    fields = ['date', 'service_Type']
    
    def form_valid(self, form):
        
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Attendance Has Been Added Successfully'
        )
        return super().form_valid(form)

#ATTENDANCE DETAIL VIEW
@login_required
def AttendanceDetailView(request, pk):
    attend = MemberAttendance.objects.get(pk=pk)
    getMod = get_object_or_404(MemberAttendance, pk=pk)
    # print(over)
    getTot = list(getMod.service_set.values_list('total', flat=True))
    sumOfTot = sum(getTot)
    MemberAttendance.objects.filter(pk=pk).update(overall_total=sumOfTot)
    
    context = {
        'attend': attend,
    }
    return render(request, 'church_app/attendance/att_detail.html', context=context)


#ATTENDANCE UPDATE VIEW
class AttendanceUpdateView(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = MemberAttendance
    template_name = 'church_app/attendance/att_edit.html'
    extra_context = {'attend': model,}

   
    def get_success_url(self):
        return reverse('church_app:att_detail', kwargs={'pk': self.object.pk})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=MemberAttendance.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=MemberAttendance.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return MemberAttendanceServiceFormset(**self.get_form_kwargs(), instance=self.object,)

    def form_valid(self, form):
        form.save(commit=True)
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes Saved. Refresh Page to Update Overall Total'
        )
        
        return HttpResponseRedirect(self.get_success_url())
  
    














#VIEW TO CALCULATE OVERALL TOTAL OF ATTENDANCE
# @login_required
# def AttendOverall(request, pk):
    # getMod = get_object_or_404(MemberAttendance, pk=pk)
    # # print(over)
    # getTot = list(getMod.service_set.values_list('total', flat=True))
    # sumOfTot = sum(getTot)
    # # overTot = getMod(overall_total = 50)
    # # obj = get_object_or_404(MemberAttendance.objects.values_list('overall_total', flat=True).update(overall_total=50), pk=pk)
    # MemberAttendance.objects.filter(pk=pk).update(overall_total=sumOfTot)
    
    # return redirect('church_app:att_detail', pk=pk)




# # def AttFormPageView(request):
#     aform = MemberAttendanceForm()
#     bform = ServiceForm()

#     if request.method == 'POST':
#         aform = MemberAttendanceForm(request.POST)
#         bform = ServiceForm(request.POST)

#         if bform.is_valid():
            
#             bform.save(commit=True)
#             return redirect('/attendance')
#         else:
#             print ('ERROR! Form is Invalid')
    
#     return render(request, 'church_app/attendance/att_formpage.html', {'aform':aform, 'bform':bform})



# class MemberDeleteView(DeleteView):
#     template_name = 'church_app/member_formpage.html'
#     model = Member
#     success_url = reverse_lazy ('church_app:list')


# class MemberDetailView(DetailView):
#     model = Member
#     template_name = 'index.html'
