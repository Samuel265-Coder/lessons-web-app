
from django import forms
from .models import Subject


class StudentRegistrationForm(forms.Form):
    full_name = forms.CharField(
        max_length=150,
        label="Full name",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your full name"}
        ),
    )

    phone_number = forms.CharField(
        max_length=20,
        label="Phone number",
        widget=forms.TextInput(
            attrs={"placeholder": "e.g. 0991234567"}
        ),
    )

    school_name = forms.CharField(
        max_length=150,
        label="Current school",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your school name"}
        ),
    )

    guardian_phone = forms.CharField(
        max_length=20,
        required=False,
        label="Guardian's phone number (optional)",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter guardian's phone number"}
        ),
    )

    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.none(),
        label="Select your subjects",
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )

    message = forms.CharField(
        required=False,
        label="Additional information (optional)",
        widget=forms.Textarea(
            attrs={
                "rows": 4,
                "placeholder": "Any questions or additional information?"
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["subjects"].queryset = (
            Subject.objects.filter(is_available=True).order_by("name")
        )
