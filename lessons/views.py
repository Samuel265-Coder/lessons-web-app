from django.shortcuts import render, redirect
from .models import (
    Subject, 
    Student, 
    Application, 
    ApplicationSubject
    )

from django.db import transaction
from .forms import StudentRegistrationForm


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

def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                student = Student.objects.create(
                    full_name=form.cleaned_data["full_name"],
                    phone_number=form.cleaned_data["phone_number"],
                    school_name=form.cleaned_data["school_name"],
                    guardian_phone=form.cleaned_data["guardian_phone"],
                )

                application = Application.objects.create(
                    student=student,
                    message=form.cleaned_data["message"],
                )

                selected_subjects = form.cleaned_data["subjects"]

                ApplicationSubject.objects.bulk_create([
                    ApplicationSubject(
                        application=application,
                        subject=subject,
                        fee_at_application=subject.fee,
                    )
                    for subject in selected_subjects
                ])

            return render(
                request,
                "lessons/registration-success.html",
                {"application": application},
            )

    else:
        form = StudentRegistrationForm()

    return render(
        request,
        "lessons/registration-form.html",
        {"form": form},
    )


