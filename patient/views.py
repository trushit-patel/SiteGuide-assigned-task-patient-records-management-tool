from django.http.response import HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from .forms import PatientRegister
from .models import Patient

def load_create(request):
    if request.method == 'POST':
        form = PatientRegister(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/display')
    else:
        form = PatientRegister()
    return render(request,'create.html',{ 'form':form })
def load_data(request):
    p_data = Patient.objects.all()
    return render(request,'display.html',{ 'p_data':p_data })
#del
def del_entry(request,pk):
    if request.method == 'POST':
        entry = Patient.objects.get(patient_id=pk)
        entry.delete()
    return HttpResponseRedirect('/display')

#update
def update_entry(request,pk):
    if request.method == 'POST':
        entry = Patient.objects.get(patient_id=pk)
        form1 = PatientRegister(request.POST,instance=entry)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect('/display')
        else:
            entry = Patient.objects.get(patient_id=pk)
            form1 = PatientRegister(instance=entry)
    else:
        entry = Patient.objects.get(patient_id=pk)
    return render(request,'update.html', {'entry':entry , 'form1':form1})
# Create your views here.