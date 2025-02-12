from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, DepartmentViewSet, AdmissionViewSet, MarksViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'admissions', AdmissionViewSet)
router.register(r'marks', MarksViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
