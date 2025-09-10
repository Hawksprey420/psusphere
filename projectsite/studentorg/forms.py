from django.forms import ModelForm
from studentorg.models import Organization, OrgMember, Student, College, Program
from .models import OrgMember
from django import forms

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = '__all__'
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'organization': forms.Select(attrs={'class': 'form-control'}),
            'date_joined': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
        }

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__"

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = "__all__"
