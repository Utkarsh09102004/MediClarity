from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import PatientLoginForm, DoctorLoginForm

def patient_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            aadhar_number = form.cleaned_data['aadhar_number']
            password = form.cleaned_data['password']
            user = authenticate(request, aadhar_number=aadhar_number, password=password)
            if user is not None and user.is_patient:
                login(request, user)
                # Redirect to patient dashboard or any other page
                print('hello')
            else:
                # Invalid login
                return render(request, 'patient_login.html', {'form': form, 'error': True})
    else:
        form = PatientLoginForm()
    return render(request, 'patientLogin', {'form': form, 'error': False})

def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            aadhar_number = form.cleaned_data['aadhar_number']
            password = form.cleaned_data['password']
            user = authenticate(request, aadhar_number=aadhar_number, password=password)
            if user is not None and user.is_doctor:
                login(request, user)
                # Redirect to doctor dashboard or any other page
                print("hello")
                # return redirect('doctor_dashboard')
            else:
                # Invalid login
                return render(request, 'doctor_login.html', {'form': form, 'error': True})
    else:
        form = DoctorLoginForm()
    return render(request, 'doctorLogin', {'form': form, 'error': False})

from .forms import PatientSignUpForm, DoctorSignUpForm
from .models import User, Patient, Doctor

def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            # Create a new user
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                aadhar_number=form.cleaned_data['aadhar_number']
            )
            user.is_patient = True
            user.save()

            # Create a new patient profile
            patient = Patient.objects.create(
                user=user,
                date_of_birth=form.cleaned_data['date_of_birth'],
                gender=form.cleaned_data['gender'],
                contact_information=form.cleaned_data['contact_information']
            )

            # Log in the user
            login(request, user)

            # Redirect to patient dashboard or any other page
            print("hello")
    else:
        form = PatientSignUpForm()
    return render(request, 'base/patient_signup.html', {'form': form})

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            # Create a new user
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                aadhar_number=form.cleaned_data['aadhar_number']
            )
            user.is_doctor = True
            user.save()

            # Create a new doctor profile
            doctor = Doctor.objects.create(
                user=user,
                specialization=form.cleaned_data['specialization'],
                contact_information=form.cleaned_data['contact_information']
            )

            # Log in the user
            login(request, user)

            # Redirect to doctor dashboard or any other page
            print("hello")
    else:
        form = DoctorSignUpForm()
    return render(request, 'doctor_signup.html', {'form': form})