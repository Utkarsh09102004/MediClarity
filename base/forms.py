# forms.py
from django import forms

class PatientLoginForm(forms.Form):
    aadhar_number = forms.CharField(label='Aadhar Number', max_length=12)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class DoctorLoginForm(forms.Form):
    aadhar_number = forms.CharField(label='Aadhar Number', max_length=12)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class PatientSignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    aadhar_number = forms.CharField(label='Aadhar Number', max_length=12)
    date_of_birth = forms.DateField(label='Date of Birth')
    gender = forms.ChoiceField(label='Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    contact_information = forms.CharField(label='Contact Information', max_length=100)

class DoctorSignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    aadhar_number = forms.CharField(label='Aadhar Number', max_length=12)
    specialization = forms.CharField(label='Specialization', max_length=100)
    contact_information = forms.CharField(label='Contact Information', max_length=100)

