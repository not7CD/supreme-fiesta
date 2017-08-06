# import individual/individual
from datetime import date, timedelta
from data_model.individual import Individual
from data_model.shift import create_shift





# def create_shift_datetime(start_dt, end_dt):
#     return create_shift()

if __name__ == '__main__':
    SHIFT_LENGTH = timedelta(hours=8)
    print(SHIFT_LENGTH)
    schedule = []

    for day in range(7):
        schedule.append(create_shift(
        date.today() + timedelta(days=day), timedelta(hours=6), timedelta(hours=8)))

    that_guy = Individual('Jan Kowalski', schedule)
    print(that_guy)
    # main()
