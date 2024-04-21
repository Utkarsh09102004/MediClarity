from django.urls import path
from .views import *

urlpatterns = [
    path('doctor-login/', doctor_login, name='doctorlogin'),
    path('patient-login/', patient_login, name='patientlogin'),
    path('doctor-signup/', doctor_signup, name='doctorSignup'),
    path('patient-signup/',patient_signup, name='patientSignup'),
    path('doctor-dashboard/', doctor_dashboard, name='doctorDashboard'),
    path('patient-dashboard/', patient_details, name='patientDetails'),
]
