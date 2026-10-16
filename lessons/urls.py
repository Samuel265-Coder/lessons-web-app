from django.urls import path
from lessons.views import subject

urlpatterns = [
    path("subjects/", subject, name="subject")
]