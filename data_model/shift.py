from datetime import datetime as dt

def create_shift(shift_date, start_time, length):
    return {'datetime': dt.combine(shift_date, dt.min.time()) + start_time,
            'workhours': length}
