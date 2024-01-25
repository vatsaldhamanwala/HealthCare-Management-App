from rest_framework import serializers
from .models import Patient, HealthRecord, Admission, Doctor

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model =Patient
        fields= '__all__'

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model =HealthRecord
        fields= '__all__'

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model =Admission
        fields= '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model =Doctor
        fields= '__all__'

