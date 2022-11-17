from django import forms
from django.forms import fields, widgets
from .models import Patient

class PatientRegister(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['firstname','lastname','gender','age','disease','doctor','fees','medicine_date']
        CHOICES = [('M','Male'),('F','Female')]
        widgets = {
            'firstname' : forms.TextInput(attrs={'class':'form-control'}),
            'lastname' : forms.TextInput(attrs={'class':'form-control'}),
            'gender' : forms.RadioSelect(attrs={'class':'radio'},choices=CHOICES),
            'age' : forms.NumberInput(attrs={'class':'form-control'}),
            'disease' : forms.TextInput(attrs={'class':'form-control'}),
            'doctor' : forms.TextInput(attrs={'class':'form-control'}),
            'fees' : forms.NumberInput(attrs={'class':'form-control'}),
            'medicine_date' : forms.DateInput(attrs={'class':'form-control','type':'date','value':'yyyy-MM-dd','onkeyup':'fn1()'},format='%y/%m/%d'),
        }