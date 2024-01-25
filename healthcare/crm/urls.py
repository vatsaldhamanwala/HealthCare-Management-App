from django.urls import path
from .views import PatientListCreateView, HealthRecordListCreateView, AdmissionListCreateView, DoctorListCreateView, PatientDetailView, HealthRecordDetailView, AdmissionDetailView, DoctorDetailView

urlpatterns=[
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name= 'patient-detail'),
    path('health-records/', HealthRecordListCreateView.as_view(), name='health-record-list-create'),
    path('health-records/<int:pk>/', HealthRecordDetailView.as_view(), name= 'health-record-detail'),
    path('admission/', AdmissionListCreateView.as_view(), name='admission-list-create'),
    path('admission/<int:pk>/', AdmissionDetailView.as_view(), name= 'admission-detail'),
    path('doctor/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name= 'doctor-detail'),
    
]