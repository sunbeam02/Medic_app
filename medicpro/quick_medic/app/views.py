from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView, FormView

from .models import (
    Doctor,
    RequestConsulation,
    Appointment,
    Symptoms,
    Drugs,
    MedicalHistory,
    Specialization,
)

# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse('This is Home page')


class CreateDoctor(CreateView):
    model = Doctor
    fields = "__all__"
    exclude = ['is_verified', 'is_booked']
    success_url = "/"

class CreateSpecialization(CreateView):
    model = Specialization
    fields = "__all__"

class SpecializationDetail(DetailView):
    model = Specialization

class SpecializationList(ListView):
    model = Specialization

class Specialization():
    pass



