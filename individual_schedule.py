import csv

class person(object):
    """docstring for person."""
    def __init__(self, name):
        super(person, self).__init__()
        self.name = name
        self.shedule = []


def mine_row(row, shifts):
    pass

def get_shifts(reader):
    pattern = r'\d+\D\d+'
    for row in reader:
        # use re.filter z re.match
        pass

def miner():
    grafik_tab = []
    # NOTE: open jest standardowe więc utf-8?
    with open('data/formated/grafik.csv') as csvfile:

        grafikreader = csv.reader(csvfile)

        for row in grafikreader:
            grafik_tab.append(row[1::2])
        print(grafik_tab)
        for row in grafik_tab:
            print(list(zip(grafik_tab[2], row)))

def main():
    miner()

if __name__ == '__main__':
    main()
