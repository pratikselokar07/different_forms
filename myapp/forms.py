from django import forms
from django.core.validators import RegexValidator
from .models import Student
from django.forms import modelformset_factory

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','phone']

class StudentBasicForm(forms.Form):
    name=forms.CharField(label='Your Name')
    email=forms.EmailField(label='Your Email')
    phone=forms.CharField(label='Your Phone')


StudentModel_FormSet = modelformset_factory(Student, fields=('name', 'email', 'phone'),extra=1)