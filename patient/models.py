from django.db import models

class Patient(models.Model):
    patient_id = models.AutoField(db_column='patientid',primary_key=True,null=False, unique=True)
    firstname = models.CharField(db_column='firstname',max_length=70,null=False)
    lastname = models.CharField(db_column='lastname',max_length=100,null=False)
    gender = models.CharField(db_column='gender',max_length=70,null=False)
    age = models.IntegerField(db_column='age',null=False)
    disease = models.CharField(db_column='disease',null=False, max_length=70)
    doctor = models.CharField(db_column='doctor',null=False, max_length=70)
    fees = models.FloatField(db_column='fees',null=False,default=500.00)
    medicine_date = models.DateField(db_column='medicine_date', null=False)

# Create your models here.
