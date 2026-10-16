from django.contrib import admin
from lessons.models import (
    Subject,
    Student,
    Application,
    ApplicationSubject,
)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "fee", "lesson_days", "venue", "is_available",)
    list_filter = ("is_available",)
    search_fields = ("name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "school_name",)
    search_fields = ("full_name", "school_name",)


class ApplicationSubjectInline(admin.TabularInline):
    model = ApplicationSubject
    extra = 1


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "applied_at", "status",)
    list_filter = ("status", "applied_at")
    search_fields = ("student__full_name",)
    inlines = [ApplicationSubjectInline]


@admin.register(ApplicationSubject)
class ApplicationSubjectAdmin(admin.ModelAdmin):
    list_display = ("application", "subject", "fee_at_application", )
    list_filter = ("subject",)
