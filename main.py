import csv

import phonebook_processor as pp

if __name__ == "__main__":
    with open('phonebook_raw.csv') as f:
        rows = csv.reader(f, delimiter=',')
        contact_list = list(rows)

    phonebook_duplicates = pp.create_contact_list(contact_list)
    fixed_phonebook = pp.phonebook_unique(phonebook_duplicates)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(fixed_phonebook)