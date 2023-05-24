from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Localty(models.Model):
    pass

class Doctor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    speciality = models.CharField(choices=SPECIALITY)
    portfolio_number = models.CharField(max_length)
    email = models.EmailField()
    phone = models.CharField()
    is_verified = models.BooleanField(default=False)
    is_booked = models.BooleanField(defult=False)

    def  get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return


class Patience(models.Model):
    pass

class Appointment(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE, related_name='my_appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    reason = models.TextField()
    date = models.DateTimeField(verbose_names="Date and Time for appointment")