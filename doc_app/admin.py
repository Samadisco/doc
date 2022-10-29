from django.contrib import admin
from .models import vitals, case_history, patient_profile




# Register your models here.


class Rendering_vitals(admin.ModelAdmin):
    list_display = ('details','temp','bp','pulse')


class Rendering_case_history(admin.ModelAdmin):
    list_display = ('cc','dur','rel','fre','asso','loc', 'lat','onset', 'pain', 'p_medix', 'e_f')   


class Rendering_patient_profile(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','dob','occupation','date_time','address','contact')    


admin.site.register(vitals,Rendering_vitals)
admin.site.register(case_history, Rendering_case_history)
admin.site.register(patient_profile,Rendering_patient_profile)