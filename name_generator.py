import os
import csv
import random


def get_names_starting_with(letter):
    names_dir = './static/navne/drenge-navne'
    fp = os.path.abspath(names_dir)
    csv_file = open(f"{os.path.join(fp, letter)}.csv", "r")
    reader = csv.reader(csv_file)
    names = []
    for name in reader:
        names.append(name[0])
    return names


def select_random_name_from_list(names):
    random_index = random.randint(0, len(names) - 1)
    randomly_selected_name = names[random_index]
    return randomly_selected_name


def get_names(letters="abcdefghijklmnopqrstuvxyzøå"):
    names = []
    for letter in letters:
        for n in get_names_starting_with(letter):
            names.append(n)
    random.shuffle(names)
    return names