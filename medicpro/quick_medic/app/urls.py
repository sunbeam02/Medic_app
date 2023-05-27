from django.urls import path, include
from .views import (
    Home,
    CreateDoctor, DoctorDetail, DoctorList, RemoveDoctor, UpdateDoctor,
    CreateSpecialization, SpecializationDetail, SpecializationList, RemoveSpecialization, UpdateSpecialization,
    CreateRequest, RequestDetail, RequestList, RemoveRequest, UpdateRequest,
    CreateAppointment,AppointmentDetail, AppointmentList, RemoveAppointment, UpdateAppointment,
    ) 

urlpatterns = [
    path('', Home.as_view(), name='home'),

    # DOCTOR URLS
    path('doctor/', include(
        [
            path('', CreateDoctor.as_view(), name="create-doctor"),
            path('<pk>', DoctorDetail.as_view(), name="doctor_detail"),
            path('<pk>/remove', RemoveDoctor.as_view(), name="doctor_remove"),
            path('<pk>/update', UpdateDoctor.as_view(), name="doctor_update"),
            path('list', DoctorList.as_view(), name="doctor_list"),
        ])),

    # REQUESTCONSULTANCY URLS
    path('request/', include(
        [
            path('', CreateRequest.as_view(), name="create-request"),
            path('<pk>', RequestDetail.as_view(), name="request_detail"),
            path('list', RequestList.as_view(), name="request_list"),
            path('<pk>/remove', RemoveRequest.as_view(), name="request_remove"),
            path('<pk>/update', UpdateRequest.as_view(), name="request_update"),
            path('list', RequestList.as_view(), name="request_list"),
        ])),

    # APPOINTMENT URLS
    path('appointment/', include(
        [
            path('', CreateAppointment.as_view(), name="create-appointment"),
            path('<pk>', AppointmentDetail.as_view(), name="appointment_detail"),
            path('list', AppointmentList.as_view(), name="appointment_list"),
            path('<pk>/remove', RemoveAppointment.as_view(), name="appointment_remove"),
            path('<pk>/update', UpdateAppointment.as_view(), name="appointment_update"),
            
        ])),

    
    # SPECIALIZATION URLS
    path('specialization/', include(
        [
            path('', CreateSpecialization.as_view(), name="create_specialization"),
            path('<pk>', SpecializationDetail.as_view(), name="specialization_detail"),
            path('<pk>/remove', RemoveSpecialization.as_view(), name="specialization_remove"),
            path('<pk>/update', UpdateSpecialization.as_view(), name="specialization_update"),
            path('list', SpecializationList.as_view(), name="specialization_list"),
        ])),

    #DRUGS URLS

    
]