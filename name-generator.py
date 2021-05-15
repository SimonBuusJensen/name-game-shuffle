import os
import csv
import random

names_dir = "static/names/"


def get_names_starting_with(letter):
    csv_file = open(f"{os.path.join(names_dir, letter)}.csv", "r")
    reader = csv.reader(csv_file)
    names = []
    for name in reader:
        names.append(name[0])
    return names


def select_random_name_from_list(names):
    random_index = random.randint(0, len(names) - 1)
    randomly_selected_name = names[random_index]
    return randomly_selected_name
