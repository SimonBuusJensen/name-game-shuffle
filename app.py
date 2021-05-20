from flask import Flask, render_template
from name_generator import get_names_starting_with, select_random_name_from_list

app = Flask(__name__)

letters = "abcdefghijklmnopqrstuvxyzøå"


def get_names():
    names = []
    for letter in letters:
        for n in get_names_starting_with(letter):
            names.append(n)
    return names


def select_n_names(names, n=3):
    selected = []
    while len(selected) < n:
        selected.append(select_random_name_from_list(names))
    return selected


@app.route('/')
def index():
    names = get_names()
    selected = select_n_names(names, 3)
    return render_template('index.html', name1=selected[0], name2=selected[1], name3=selected[2])


if __name__ == '__main__':
    app.run()
