import re
import csv
from pprint import pprint

with open('phonebook_raw.csv') as f:
    rows = csv.reader(f, delimiter=',')
    contact_list = list(rows)

for lst in contact_list:
    for cnt in range(4):
        name = re.findall(r"\w+", str(lst))[cnt]
    pprint(name)

    email = re.findall(r"[a-zA-Z0-9.-]+@[a-zA-Z.-]+\.(?:ru|com|gov|org|net)", str(lst))