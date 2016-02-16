import csv


class Controller:
    def __init__(self):
        self.reader = None
        self.delimiter = None

    def fill(self):
        text = ''
        delimiter = ';'

        with open('Mappe1.csv', newline='') as f:
            reader = csv.reader(f, delimiter=';', quotechar=' ')

            for row in reader:
                text += str(row)+'\n'
