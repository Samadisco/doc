data={'csrfmiddlewaretoken': ['nwGoQ7ARGE1KqFWB13MflQLlBI7UylttXCjgI3SRSc3UNUijGNOm4azooiuMaJ7I'], 'vitals': ['{"temperature":"10","bp":"120mmHg","pulse":"75bpm"}'], 'case_history': ['{}'], 'patient_profile': ['{"firstName":"SAMUEL","lastName":"AFARI","otherNames":"Andy","DOB":"2022-10-28","gender":"F","occupation":"Doctor","address":"Musuku-Accra","contact":"0545559960"}']}


# Working on vitals
main_split =  str(data['vitals']).split(',')

# temperature
print(main_split[0].split(':'))