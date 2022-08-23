from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django import forms

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
    