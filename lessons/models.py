
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    lesson_days = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    fee = models.DecimalField( max_digits=10, decimal_places=2,)
    venue = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    school_name = models.CharField(max_length=150)
    guardian_phone = models.CharField( max_length=20,blank=True,)

    def __str__(self):
        return self.full_name


class Application(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACCEPTED = "ACCEPTED", "Accepted"
        REJECTED = "REJECTED", "Rejected"

    student = models.ForeignKey( Student,on_delete=models.CASCADE, related_name="applications",)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING,)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"Application by {self.student.full_name}"


class ApplicationSubject(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="selected_subjects",)
    subject = models.ForeignKey(Subject,  on_delete=models.PROTECT,related_name="application_selections", )
    fee_at_application = models.DecimalField(max_digits=10, decimal_places=2, )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["application", "subject"],
                name="unique_subject_per_application",
            )
        ]

    def __str__(self):
        return (f"{self.application.student.full_name} - {self.subject.name}")
