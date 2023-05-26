from django.urls import path
from .views import (
    Home,
    CreateDoctor,
    CreateSpecialization,
    SpecializationDetail,
    SpecializationList,
    ) 

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('doctor', CreateDoctor.as_view(), name="create-doctor"),
    path('specialization', CreateSpecialization.as_view(), name="create_specialization"),
    path('specialization/<pk>', SpecializationDetail.as_view(), name="specialization_detail"),
    path('specialization/all', SpecializationList.as_view(), name="specialization_list"),
]