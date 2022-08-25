from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from . import models

# Create your views here.

def index(request):
    return render(request,'dashboard/dashboard.html')

class StationAirQualityCreate(CreateView):
    model = models.StationAirQuality
    fields = '__all__'

    def get_form(self,form_class=None):
        form = super().get_form(form_class)
        form.fields["Date"].widget = forms.DateInput(format=('%d/%m/%Y'),attrs={'class':'form_control','placeholder':'Select a date','type':'date'})
        return form

class RouteWiseDataCreate(CreateView):
    model = models.RouteWiseData
    fields = '__all__'

    def get_form(self,form_class=None):
        form = super().get_form(form_class)
        form.fields["Date"].widget = forms.DateInput(format=('%d/%m/%Y'),attrs={'class':'form_control','placeholder':'Select a date','type':'date'})
        return form
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'