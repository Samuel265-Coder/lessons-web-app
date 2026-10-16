from django.shortcuts import render
from .models import Subject


def subject(request):
    subjects = Subject.objects.filter(
        is_available=True
    ).order_by("name")

    context = {
        "subjects": subjects,
    }

    return render(
        request,
        "lessons/subjects-list.html",
        context,
    )