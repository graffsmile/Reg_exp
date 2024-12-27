import os
from os.path import split
from pprint import pprint
import csv
import re

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


  # TODO 2: сохраните получившиеся данные в другой файл
  # код для записи файла в формате CSV
def write(new_file, dict):
    # contacts = splited_name
    keys = list(dict[0].keys())
    with open(new_file, "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
        datawriter.writerows(keys)
        for items in dict:
            datawriter.writerows(items)
        # return datawriter.writerows(contacts)

if __name__ == '__main__':
    file_name = 'phonebook_raw.csv'
    new_file = 'phonebook.csv'

    phones_fixed(file_name, n_file='nfile.csv')
    splited_name = split_name(file_name='nfile.csv')
    os.remove('nfile.csv')
    pprint(splited_name)
    write(new_file, splited_name)