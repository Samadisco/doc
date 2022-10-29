from pickle import TRUE
from tabnanny import verbose
from django.db import models


# Create your models here.

class patient_profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.CharField(max_length =10)
    gender = models.CharField(max_length =10)
    occupation = models.CharField(max_length =50)
    address =  models.CharField(max_length =100)
    contact = models.CharField(max_length =100)
    id = models.CharField(max_length =20, primary_key = TRUE)
    date_time = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Patient Profile'
  
    def __str__(self):
        return self.id +' '+ str(self.first_name)




class vitals(models.Model):
    
    temp = models.CharField(max_length=10)
    bp = models.CharField(max_length=10)
    pulse = models.CharField(max_length=10)
    details = models.ForeignKey(patient_profile, on_delete = models.CASCADE)
    

    class Meta:
        verbose_name_plural = 'Vitals'
    def __str__(self):
        return (self.temp) + ' ' + str(self.details.first_name)

        


class case_history(models.Model):
    cc = models.CharField(max_length =200)
    dur = models.CharField(max_length =200)
    rel =  models.CharField(max_length =200)
    fre = models.CharField(max_length =200)
    asso = models.CharField(max_length =200)
    loc = models.CharField(max_length =200)
    lat = models.CharField(max_length =100)
    onset = models.CharField(max_length =200)
    pain = models.CharField(max_length =100)
    p_medix = models.CharField(max_length =200)
    e_f = models.CharField(max_length =100)
    details = models.ForeignKey(patient_profile, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Case History'
    def __str__(self):
        return self.cc
        



































