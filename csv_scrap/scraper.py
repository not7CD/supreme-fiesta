import csv, re
from datetime import datetime
from data_model.shift import dict_to_shift

def open_csv(path):
    file_date = re.search("([0-9]{4}\-[0-9]{2}\-[0-9]{2})", path)
    shift_date = datetime.strptime(file_date.group(1), '%Y-%m-%d').date()

    shifts_with_name = []
    with open(path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            shifts_with_name.append(dict_to_shift(shift_date, row))

    return shifts_with_name
