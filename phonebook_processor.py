import re
import csv
from pprint import pprint

with open('phonebook_raw.csv') as f:
    rows = csv.reader(f, delimiter=',')
    contact_list = list(rows)

new_contact_list = []
for lst in contact_list[1:]:
    fio_pos = re.findall(r"[а-яА-Я]+", str(lst[0:4]))
    for i in range(0, len(fio_pos)):
        lastname = re.findall(r"[а-яА-Я]+", str(lst))[i]
        # pprint(lastname)
    position = re.findall(r".+", str(lst[4]))
    # phone = re.findall(r"(?:\+7\s*|8\s*)?\(*\s*\d+\)*\s*\d+[-\s]*\d+[-\s]*\d+"
    #                    r"[-\s]*\(*[\w.]*\s*\d+\)*", str(lst))
    phone = re.findall(r"(?:\+7\s*|8\s*)?\(*\s*(\d+)\)*\s*(\d+)[-\s]*(\d+)[-\s]*(\d+)"
                       r"[-\s]*\(*[\w.]*\s*(\d+)\)*", str(lst))

    email = re.findall(r"(?:\w+|\d+|\.|-)@\w+\.\w+", str(lst))
    pprint(phone)

    # --alternatives--
    # surname = re.findall(r"\w+(?:вич|вна)", str(lst))
    # email = re.findall(r"[a-zA-Z0-9.-]+@[a-zA-Z.-]+\.(?:ru|com|gov|org|net)", str(lst))
