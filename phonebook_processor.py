import re
import csv
from pprint import pprint

with open('phonebook_raw.csv') as f:
    rows = csv.reader(f, delimiter=',')
    contact_list = list(rows)

phone_pattern = r"(\+7|8)?[\s-]?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})\s?\(?(доб\.?)?\s?(\d+)?\)?"
phone_substitute = r"+7(\2)\3-\4-\5 \6\7"


def phone_format(pat, sub, col_ind=5):
    phone_new = re.sub(pat, sub, str(lst[col_ind]))
    phone_new = phone_new.strip(' ')
    if phone_new == '':
        phone_new = []
        return phone_new
    else:
        return [phone_new]


new_contact_list = [contact_list[0]]
for lst in contact_list[1:]:
    person = []
    elem_in_entry_range = lst[0:4]
    fio_dept_re = re.findall(r"[а-яА-Я]+", str(elem_in_entry_range))
    if len(fio_dept_re) < len(elem_in_entry_range):
        delta = len(elem_in_entry_range) - len(fio_dept_re)
        for i in range(delta):
            fio_dept_re.append([])
    person.extend(fio_dept_re)

    position = re.findall(r".+", str(lst[4]))
    person.append(position)

    phone = phone_format(phone_pattern, phone_substitute)
    person.append(phone)
    email = re.findall(r"(?:\w+|\d+|\.|-)@\w+\.\w+", str(lst))
    person.append(email)

    for i in range(len(person)):
        if len(person[i]) == 1:
            person[i] = person[i][0]
        elif not person[i]:
            person[i] = ''
    new_contact_list.append(person)

print(new_contact_list)


    # --alternative regex--
    # surname = re.findall(r"\w+(?:вич|вна)", str(lst))
    # email = re.findall(r"[a-zA-Z0-9.-]+@[a-zA-Z.-]+\.(?:ru|com|gov|org|net)", str(lst))
