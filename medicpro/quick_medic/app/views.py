from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

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
    
   #CREATE USER 
class CreateUser(View):
    def post(self, request):
        content_type = ContentType.objects.get_for_model(User)
        user_permission = Permission.object.filter(content_type = content_type)
        user = User(username = 'url', first_name="deji", last_name="sun", password="1234")
        user.user_permissions.add(user_permission)
        user.save()
    
    #DOCTOR VIEW
class CreateDoctor(CreateView):
    model = Doctor
    fields = "__all__"
    exclude = ['is_verified', 'is_booked']
    success_url = "/"

class DoctorDetail(PermissionRequiredMixin, DetailView):
    model = Doctor
    permission_required = ("app.can_view_doctor_detail")

class DoctorList(ListView):
    model = Doctor

class RemoveDoctor(LoginRequiredMixin, DeleteView):
    model = Doctor
    login_url = "/"

class UpdateDoctor(UpdateView):
    model = Doctor
    fields = "__all__"


#SPECIALIZATION VIEWS
class CreateSpecialization(CreateView):
    model = Specialization
    fields = "__all__"

class SpecializationDetail(PermissionRequiredMixin, DetailView):
    model = Specialization

class SpecializationList(ListView):
    model = Specialization

class RemoveSpecialization(LoginRequiredMixin, DeleteView):
    model = Specialization
    login_url = "/"

class UpdateSpecialization(UpdateView):
    model = Specialization
    fields = "__all__"


# for Request
class CreateRequest(CreateView):
    model = RequestConsulation
    fields = "__all__"
    template_name = "app/doctor_form.html"

class RequestDetail(PermissionRequiredMixin, DetailView):
    model = RequestConsulation
    permission_required = ['can_consult']

class RequestList(ListView):
    model = RequestConsulation

class RemoveRequest(LoginRequiredMixin, DeleteView):
    model = RequestConsulation
    login_url = "/"

class UpdateRequest(UpdateView):
    model = RequestConsulation
    fields = "__all__"

# for APPOINTMENT
class CreateAppointment(CreateView):
    model =  Appointment
    template_name = "doctor_form.html"
    fields = "__all__"

class AppointmentDetail(PermissionRequiredMixin, DetailView):
    model =  Appointment

class AppointmentList(ListView):
    model =  Appointment

class RemoveAppointment(LoginRequiredMixin, DeleteView):
    model =  Appointment
    login_url = "/"

class UpdateAppointment(UpdateView):
    model = Appointment
    


