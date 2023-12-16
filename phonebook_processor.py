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
    return phone_new


new_contact_list = []
for lst in contact_list[1:]:
    fio_pos = re.findall(r"[а-яА-Я]+", str(lst[0:4]))
    for i in range(0, len(fio_pos)):
        lastname = re.findall(r"[а-яА-Я]+", str(lst))[i]
    position = re.findall(r".+", str(lst[4]))
    phone = phone_format(phone_pattern, phone_substitute)
    email = re.findall(r"(?:\w+|\d+|\.|-)@\w+\.\w+", str(lst))
    pprint(email)

    # --alternatives--
    # surname = re.findall(r"\w+(?:вич|вна)", str(lst))
    # email = re.findall(r"[a-zA-Z0-9.-]+@[a-zA-Z.-]+\.(?:ru|com|gov|org|net)", str(lst))
