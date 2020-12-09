import os
import csv

from autocom.models import Customer


custs = open('autocom/custs.csv')
r = csv.reader(custs)
for last, first, number in r:
    c = Customer.objects.create(first_name=first, last_name=last, random_number=number)
    c.save()
    print(f"Added {first} {last} to customer list")
