from django.contrib import admin
from django.urls import include, path
from patient import views as vwpatient

urlpatterns = [
    path('', include('myproject.core.urls', namespace='core')),
    path('accounts/', include('myproject.accounts.urls')),
    path('endValidation/', vwpatient.endValidation, name='endValidation'),
    path('admin/', admin.site.urls),
    path('records/', vwpatient.db_record, name='records'),
    path('recordsAcIn/<int:status>', vwpatient.db_record_status, name='recordsAcIn'), #Ativo = 1 Inativo = 0 
    path('disable/<int:ValueId>', vwpatient.disablePatient, name='disable'),
    path('validation_group/<int:validateNumb>', vwpatient.validation_group, name='validation_group'),
    path('makeGroups/', vwpatient.makeGroups, name='makeGroups'),
    path('justification/', vwpatient.justification, name='justification'),
    #path('justification/<int:Id, int:group_patient>', vwpatient.justification, name='justification'),
    
    

]
