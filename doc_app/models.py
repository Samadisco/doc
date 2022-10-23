from django.db import models


# # Create your models here.

# class patient_profile(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     other_names = models.CharField(max_length=50)
#     departure_date = models.DateField()
#     gender = models.CharField(max_length=20)
#     phone_no = models.CharField(max_length=30)
#     std_id = models.CharField(max_length=10)

#     def __str__(self):
#         return self.std_id



# class trip_info(models.Model):
   
#     trip_id = models.CharField(max_length=10)
#     std_id = models.CharField(max_length=10)
#     departure_date = models.DateField()
#     departure_time = models.CharField(max_length=10)
#     destination = models.CharField(max_length=50)
#     ticket_id = models.CharField(max_length=50)
#     seat_number = models.CharField(max_length=50, default='Nill')
#     full_name = models.CharField(max_length=60)

#     def __str__(self):
#         return (self.ticket_id) +' '+ str(self.pk)

        


# class bus_info(models.Model):
#     current_bus_number = models.CharField(max_length=50,default='Nill')

#     def __str__(self):
#         return self.current_bus_number



































