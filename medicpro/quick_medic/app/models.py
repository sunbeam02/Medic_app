from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
STATUS =(('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined'))

class Location(models.Model):
    pass

class Specialization(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("specialization_detail", kwargs={"pk": self.pk})

class Doctor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    speciality = models.ForeignKey(Specialization, on_delete=models.SET_DEFAULT, null=True,default=None)
    portfolio_number = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    is_booked = models.BooleanField(default=False)

    def  get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.specialty.name}"

class Patient(models.Model):
    pass

class RequestConsulation(models.Model):
    """ Patience request consultation with available doctor, the doctor sets appointment if consultation is accepted """
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    doctor = models.ForeignKey(Doctor, related_name="consultations", verbose_name="Request for consultation", on_delete=models.CASCADE)
    symptoms = models.TextField()
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self) -> str:
        return f"{self.patient}-{self.status}"
    class Meta:
        permissions = (('can_consult'), 'COnsult Doctor')

class Appointment(models.Model):
    consult = models.ForeignKey(RequestConsulation, on_delete=models.CASCADE)
    type = models.CharField(max_length=200, choices=(('virtual','Virtual'), ('physical', 'Physical'), ('private','Private')))
    date = models.DateTimeField(verbose_name="Date and Time for appointment")

    def __str__(self)-> str:
        return f"{self.type} {self.date}"

class Symptoms(models.Model):
    name = models.CharField(max_length=200, verbose_name="symptoms")

    def __str__(self) -> str:
        return self.name
    
class Drugs(models.Model):
    name = models.CharField(max_length=200, verbose_name="name of the drug")
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Medical History", related_name="medical_history")
    illness = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptoms)
    drugs = models.ManyToManyField(Drugs)
    allergies = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Patients Attended", related_name='medical_history')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.illness} - {self.doctor} - {self.date}"