from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .inputData import storeDb
from .forms import PatientLoginForm, DoctorLoginForm
from .models import MedicalHistory, Prescription
from .inputData import create_patient_record_from_json

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
    return render(request, 'base/patient_login.html', {'form': form, 'error': False})
@csrf_exempt
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
                return render(request, 'base/doctor_login.html', {'form': form, 'error': True})
    else:
        form = DoctorLoginForm()
    return render(request, 'base/doctor_login.html', {'form': form, 'error': False})

from .forms import PatientSignUpForm, DoctorSignUpForm
from .models import User, Patient, Doctor

@csrf_exempt
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
            return redirect('doctorDashboard')
    else:
        form = DoctorSignUpForm()
    return render(request, 'base/doctor_signup.html', {'form': form})

@csrf_exempt
def doctor_dashboard(request):
    user = request.user
    doctor = Doctor.objects.get(user=user)

    if request.method == 'POST':
        aadhar_number = request.POST.get('aadhar_number')

        users = User.objects.filter(aadhar_number=aadhar_number).first()
        if users:
            request.session['data'] = aadhar_number
            return redirect('patientDetails')

        else:
            messages.error(request, 'Incorrect Aadhar number.')
            context = {'doctor': doctor, 'user': user}
    context = {'doctor': doctor, 'user': user}
    return render(request, 'base/doctor_dashboard.html', context)
@csrf_exempt
def patient_details(request):
    user = request.user
    data = request.session.get('data')
    doctor = Doctor.objects.get(user=user)
    print(data)

    patient_user = User.objects.get(aadhar_number=data)
    patient=Patient.objects.get(user=patient_user)

    if request.method == 'POST':
        transcription = request.POST.get('transcription', '')
        storeDb(patient, doctor, transcription)
        return redirect('patientDetails')

    prescriptions = Prescription.objects.filter(patient=patient)

    # Get all medical history related to the patient
    medical_history = MedicalHistory.objects.filter(patient=patient)

    # Pass the prescriptions and medical history to the context dictionary
    context = {
        'patient': patient,
        'prescriptions': prescriptions,
        'medical_history': medical_history,
    }

    # Render the template with the context

    context={"patient_user":patient_user, "doctor_user":user,"patient":patient,"prescriptions":prescriptions, "medical_history": medical_history}
    return render(request, 'base/patient_details.html',context )




