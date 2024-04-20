from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    aadhar_number = models.CharField(max_length=12, unique=True, blank=True, null=True)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='patient_profile')
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_information = models.CharField(max_length=100)
    # Medical History could be a separate table if extensive

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor_profile')
    specialization = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username



class MedicalHistory(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=100)
    date_acquired = models.DateField()

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)

class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    transcribed_text = models.TextField()

class VitalInformation(models.Model):
    vital_id = models.AutoField(primary_key=True)
    vital_name = models.CharField(max_length=100)
    description = models.TextField()

class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=100)
    description = models.TextField()

class Medication(models.Model):
    medication_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    purpose = models.TextField()

class PrescriptionDetails(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    vital_information = models.ForeignKey(VitalInformation, on_delete=models.CASCADE, null=True, blank=True)
    diseases = models.ManyToManyField(Disease, blank=True)
    medications = models.ManyToManyField(Medication, blank=True)
    value = models.CharField(max_length=100)