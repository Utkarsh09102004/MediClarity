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
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE,null=True)
    disease_name = models.CharField(max_length=100)
    date_acquired = models.DateField()

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)

class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    date = models.DateField( null=True)
    transcribed_text = models.TextField(null=True)
    disease = models.ForeignKey('MedicalCondition', on_delete=models.CASCADE, null=True)
    medications = models.ManyToManyField('Medication', related_name='prescribed_to', null=True)



class MedicalCondition(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=100)



class VitalSigns(models.Model):
    vital_id = models.AutoField(primary_key=True)
    vital_name = models.CharField(max_length=100)
    value= models.CharField(max_length=100, null=True)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)






class Medication(models.Model):
    medication_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    purpose = models.CharField(max_length=100)
    prescriptions = models.ManyToManyField('Prescription', related_name='prescribed_medications',null=True)


