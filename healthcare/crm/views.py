from rest_framework import generics
from .models import Patient, HealthRecord, Admission, Doctor
from .serializers import PatientSerializer, HealthRecordSerializer, AdmissionSerializer, DoctorSerializer


class PatientListCreateView(generics.ListCreateAPIView):
    queryset= Patient.objects.all()
    serializer_class= PatientSerializer

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Patient.objects.all()
    serializer_class= PatientSerializer

class HealthRecordListCreateView(generics.ListCreateAPIView):
    queryset= HealthRecord.objects.all()
    serializer_class= HealthRecordSerializer

class HealthRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= HealthRecord.objects.all()
    serializer_class= HealthRecordSerializer


class AdmissionListCreateView(generics.ListCreateAPIView):
    queryset= Admission.objects.all()
    serializer_class= AdmissionSerializer

class AdmissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Admission.objects.all()
    serializer_class= AdmissionSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset= Doctor.objects.all()
    serializer_class= DoctorSerializer

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Doctor.objects.all()
    serializer_class= DoctorSerializer

