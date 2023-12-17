import re
import csv
from pprint import pprint

with open('phonebook_raw.csv') as f:
    rows = csv.reader(f, delimiter=',')
    contact_list = list(rows)

fio_and_dept_pattern = r"[а-яА-Я]+"
position_pattern = r".+"
email_pattern = r"(?:\w+|\d+|\.|-)@\w+\.\w+"
phone_pattern = r"(\+7|8)?[\s-]?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})\s?\(?(доб\.?)?\s?(\d+)?\)?"
phone_substitute = r"+7(\2)\3-\4-\5 \6\7"


def fio_and_dept_extract(pat: str, txt_to_format: list, col_ind=slice(0, 4)):
    elem_in_entry_range = txt_to_format[col_ind]
    fio_dept_formatted = re.findall(pat, str(elem_in_entry_range))
    if len(fio_dept_formatted) < len(elem_in_entry_range):
        delta = len(elem_in_entry_range) - len(fio_dept_formatted)
        for el in range(delta):
            fio_dept_formatted.append('')
    return fio_dept_formatted


def phone_format_extract(pat: str, sub: str, txt_to_format: list, col_ind=5):
    phone_new = re.sub(pat, sub, str(txt_to_format[col_ind])).strip(' ')
    return [phone_new]


def placeholders_add(list_to_check: list):
    for el in range(len(list_to_check)):
        if len(list_to_check[el]) == 1:
            list_to_check[el] = list_to_check[el][0]
        elif not list_to_check[el]:
            list_to_check[el] = ''
    return list_to_check


def create_contact_list(contacts_dirty: list):
    new_contact_list = [contacts_dirty[0]]
    for lst in contacts_dirty[1:]:
        person = []

        fio_dept = fio_and_dept_extract(fio_and_dept_pattern, lst)
        person.extend(fio_dept)

        position = re.findall(position_pattern, str(lst[4]))
        person.append(position)

        phone = phone_format_extract(phone_pattern, phone_substitute, lst)
        person.append(phone)

        email = re.findall(email_pattern, str(lst))
        person.append(email)

        placeholders_add(person)
        new_contact_list.append(person)

    pprint(new_contact_list)
    return new_contact_list

create_contact_list(contact_list)

# if __name__ == "__main__":


# --alternative regex--
# surname_pattern = re.findall(r"\w+(?:вич|вна)", str(lst))
# email_pattern = re.findall(r"[a-zA-Z0-9.-]+@[a-zA-Z.-]+\.(?:ru|com|gov|org|net)", str(lst))
