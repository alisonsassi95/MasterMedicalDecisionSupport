from django.db import models

# Create your models here.
class DataPatient(models.Model):
    name_patient = models.CharField(max_length=200)
    neurological = models.IntegerField()
    MeaningNeurological = models.CharField(max_length=200)
    cardiovascular = models.IntegerField()
    MeaningCardiovascular = models.CharField(max_length=200)
    respiratory = models.IntegerField()
    MeaningRespiratory = models.CharField(max_length=200)
    coagulation = models.IntegerField()
    MeaningCoagulation = models.CharField(max_length=200)
    hepatic = models.IntegerField()
    MeaningHepatic = models.CharField(max_length=200)
    renal = models.IntegerField()
    MeaningRenal = models.CharField(max_length=200)
    spict = models.IntegerField()
    MeaningSpict = models.CharField(max_length=200)
    ecog = models.IntegerField()
    MeaningEcog = models.CharField(max_length=200)
    scoreSOFA = models.IntegerField()
    scoreAmib = models.IntegerField()
    group_patient = models.IntegerField()
    classification = models.IntegerField()
    active = models.BooleanField()
    exported = models.BooleanField()
    validatedDoctor = models.BooleanField()
    justification = models.CharField(max_length=1000)
    class Meta:
        db_table = 'patient'

    def __str__(self):
        return self.patient