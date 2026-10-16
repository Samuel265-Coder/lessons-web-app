from django.urls import path
from lessons.views import (subject, 
                           register_student
                           )

urlpatterns = [
    path("", subject, name="subject"),
    path('register/', register_student, name='register_student'),
]