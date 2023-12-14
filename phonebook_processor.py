import csv
from pprint import pprint

with open('phonebook_raw.csv') as f:
    rows = csv.reader(f, delimiter=',')
    contact_list = list(rows)
pprint(contact_list)