from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name = 'student_profile'),
    path('deleteStd/<int:id>', views.deleteStudent, name = 'student_delete'),
]
