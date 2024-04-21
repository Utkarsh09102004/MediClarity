from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Patient)
# Register your models here.
admin.site.register(Doctor)
admin.site.register(MedicalHistory)
admin.site.register(Prescription)
admin.site.register(VitalSigns)
admin.site.register(MedicalCondition)
admin.site.register(Medication)
