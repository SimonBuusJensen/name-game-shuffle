from flask import Flask, render_template, request
from name_generator import get_names

app = Flask(__name__)

names = get_names()
name_index = 0


def select_next_names():
    global name_index
    if name_index < len(names) - 2:
        name_index += 3
    selected_names = names[name_index:name_index + 3]
    return selected_names


def select_prev_names():
    global name_index
    if name_index > 2:
        name_index -= 3
    selected_names = names[name_index:name_index + 3]
    return selected_names


@app.route('/')
def index():
    selected_names = names[name_index:name_index + 3]
    return render_template('index.html', name1=selected_names[0], name2=selected_names[1], name3=selected_names[2])


@app.route('/backward')
def backward():
    selected_names = select_prev_names()
    return render_template('index.html', name1=selected_names[0], name2=selected_names[1], name3=selected_names[2])


@app.route('/forward')
def forward():
    selected_names = select_next_names()
    return render_template('index.html', name1=selected_names[0], name2=selected_names[1], name3=selected_names[2])


@app.route('/save')
def save():
    selected_names = names[name_index:name_index + 3]
    return render_template('index.html', name1=selected_names[0], name2=selected_names[1], name3=selected_names[2])


if __name__ == '__main__':
    app.run()
