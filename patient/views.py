from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import DataPatient
from django.views.decorators.csrf import csrf_exempt

from django.core.paginator import Paginator


@login_required
def endValidation(request):
    return render(request, 'endValidation.html')

@login_required
def makeGroups(request):
    results = DataPatient.objects.raw('SELECT id, count(id) as number_patient, group_patient as group_patient FROM patient WHERE active = 1 AND classification < 1 GROUP BY group_patient')
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
    patientRecords = DataPatient.objects.filter(group_patient=validateNumb).filter(active = 1).order_by('classification')
    return render(request, 'validation.html', {'patient_records': patientRecords})

@login_required
@csrf_exempt
def updateOrder(request):
    if request.method == 'POST':
        # Colocar a classificação conforme o ID
        for key, value in request.POST.items():
            idPatient = DataPatient.objects.filter(id=key).first()
            idPatient.classification = value
            idPatient.exported = 1
            idPatient.validatedDoctor = request.user.id
            idPatient.save()
        return redirect('endValidation')

@login_required
def disablePatient(request, ValueId):
    for idPatient in DataPatient.objects.filter(id=ValueId):
        idPatient.active = False
        idPatient.save()
    return redirect('records')

@login_required
@csrf_exempt
def justification(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            idPatient = DataPatient.objects.filter(id=key).first()
            idPatient.justification = value
            idPatient.active = 0
            idPatient.save()
        return redirect('endValidation')
