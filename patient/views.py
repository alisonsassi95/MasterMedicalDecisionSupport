from pickle import TRUE
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import DataPatient

from django.core.paginator import Paginator


@login_required
def makeGroups(request):
    results = DataPatient.objects.raw('SELECT id, count(id) as number_patient, group_patient as group_patient FROM patient WHERE active = 1 GROUP BY group_patient')
    print(results)
    return render(request, 'makeGroups.html', {'dataPatients': results})

@login_required
def db_record(request):
    patientRecords = DataPatient.objects.all()
    '''paginator = Paginator(patientRecords, 3)
    page = request.GET.get('page')
    patientRecords = paginator.get_page(page)
    return render(request, 'database.html', {'patientRecords':patientRecords})'''

    context = {
        'patient_records': patientRecords
    }
    return render(request, 'database.html', context)

@login_required
def db_record_status(request,status):
    if (status == 0):
        patientRecords = DataPatient.objects.filter(active = 0)
    elif (status == 1):
        patientRecords = DataPatient.objects.filter(active = 1)
    context = {
        'patient_records': patientRecords
    }
    return render(request, 'database.html', context)

@login_required
def validation_group(request, validateNumb):
    # Instensão é de pegar os dados de pacientes no Grupo passado...
    patientRecords = DataPatient.objects.filter(group_patient=validateNumb).filter(active = 1)
    return render(request, 'validation.html', {'patient_records': patientRecords})

@login_required
def disablePatient(request, ValueId):
    for idPatient in DataPatient.objects.filter(id=ValueId):
        idPatient.active = False
        idPatient.save()
    return redirect('records')
