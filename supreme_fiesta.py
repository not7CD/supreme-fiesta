# import individual/individual
from datetime import date, timedelta
from data_model.individual import Individual
from data_model.shift import create_shift
from csv_scrap.scraper import open_csv

# def create_shift_datetime(start_dt, end_dt):
#     return create_shift()

if __name__ == '__main__':
    files = ['example/2017-08-09.csv', 'example/2017-08-10.csv']

    shifts_named = []

    for file_name in files:
        shifts_named.extend(open_csv(file_name))

    for row in shifts_named:
        print(row)

    individuals = {}

    for name, shift in shifts_named:
        if name in individuals:
            individuals[name].schedule.append(shift)
        else:
            individuals[name] = Individual(name, [shift])

    print(individuals)
