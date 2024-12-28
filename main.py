import os
from idlelib.editor import keynames
from operator import itemgetter
from os.path import split
from pprint import pprint
import csv
import re
import itertools

# читаем адресную книгу в формате CSV в список contacts_list

def read_file(file_name):
    with open(file_name, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        # pprint(contacts_list)

      # TODO 1: выполните пункты 1-3 ДЗ
        keys = contacts_list[0]
        values = contacts_list[1:]
        contacts_dict = []
        for num, vals in enumerate(values):
            contacts_dict.append({})
            for key, val in zip(keys, vals):
                contacts_dict[num].update({key: val})
        return contacts_dict

def split_name(file_name):
    contacts_dict = read_file(file_name)
    for item in contacts_dict:
        split_items = item['lastname'].split(' ')
        if len(split_items) > 1:
            item['lastname'] = split_items[0]
            item['firstname'] = split_items[1]
            if len(split_items) > 2:
                item['surname'] = split_items[2]

        split_items = item['firstname'].split(' ')
        if len(split_items) > 1:
            item['firstname'] = split_items[0]
            item['surname'] = split_items[1]
    return contacts_dict


def phones_fixed(file_name, n_file):
    with open(file_name, encoding="utf-8") as f:
        text = f.read()

    pattern = r'(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?'
    fixed_phones = re.sub(pattern, r'+7(\2)\3-\4-\5\6\7\8', text)
    with open(n_file, 'w+', encoding="utf-8") as fw:
        fix = fw.write(fixed_phones)
    return fix

# def names_merges(contacts_list):


  # TODO 2: сохраните получившиеся данные в другой файл
  # код для записи файла в формате CSV
def write(new_file, dict):
    # list_dict = dict
    contacts_dict = {}
    keys = dict[0].keys()

    for contacts in dict:
        lastname = dict[1]
        firstname = dict[2]
        # surname = contacts[2]
        # organization = contacts[3]
        # position = contacts[4]
        # phone = phones_fixed(contacts[5])
        # email = contacts[6]
        # key = (lastname, firstname)
        result_list = list()
        for new_contact in dict[1:]:
            new_lastname = new_contact['lastname']
            new_firstname = new_contact['firstname']
            if lastname == new_lastname and firstname == new_firstname:
                if contacts[2] == '':
                    contacts[2] = new_contact[2]
                if contacts[3] == '':
                    contacts[3] = new_contact[3]
                if contacts[4] == '':
                    contacts[4] = new_contact[4]
                if contacts[5] == '':
                    contacts[5] = new_contact[5]
                if contacts[6] == '':
                    contacts[6] = new_contact[6]
                # result_list = list()
                if contacts not in dict:
                    result_list.append(contacts)
                # return result_list
        pprint(result_list)

    with open(new_file, "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
        datawriter.writerow(keys)
        for items in dict:
            datawriter.writerow(items.values())
        return datawriter



if __name__ == '__main__':
    file_name = 'phonebook_raw.csv'
    new_file = 'phonebook.csv'

    phones_fixed(file_name, n_file='nfile.csv')
    splited_name = split_name(file_name='nfile.csv')
    os.remove('nfile.csv')
    # pprint(splited_name)
    write(new_file, splited_name)