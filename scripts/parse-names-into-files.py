import os
import urllib.request
from bs4 import BeautifulSoup
import csv


def read_html(letter):
    url = f"https://www.babyklar.dk/drengenavn/drengenavne-med-{letter}.html"
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf-8")
    fp.close()
    return mystr


def parse_names(soup):
    return soup.findAll('p')[1].text

def format_names(names):
    formatted_names = []
    for name in names:
        name = name.strip()
        name = name.split('.')[0]
        formatted_names.append(name)
    return formatted_names

if __name__ == '__main__':


    letters = "abcdefghijklmnopqrstuvxyzøå"

    for letter in letters:

        if letter == "ø":
            letter = "oe"

        if letter == "å":
            letter = "aa"

        soup = BeautifulSoup(read_html(letter), 'html.parser')

        try:
            names = parse_names(soup).split(",")

            formatted_names = format_names(names)

            print(formatted_names)

            csv_file = open(f"/home/simon/data/navne/drenge-navne/{letter}.csv", "w")
            writer = csv.DictWriter(csv_file, fieldnames=["name"])

            for name in formatted_names:
                writer.writerow({"name": name})

            csv_file.close()

        except Exception as e:
            print(f"couldn't parse names for {letter}")


