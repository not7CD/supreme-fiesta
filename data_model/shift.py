from datetime import datetime, timedelta

def create_shift(shift_date, start_time, length):
    return {'datetime': datetime.combine(shift_date, datetime.min.time()) + start_time,
            'workhours': length}

def dict_to_shift(shift_date, shift_dict):
    name = shift_dict['name']
    start_delta = timedelta(hours=int(shift_dict['start_hour']))
    length_delta = timedelta(hours=int(shift_dict['end_hour'])) - timedelta(hours=int(shift_dict['start_hour']))
    shift = create_shift(shift_date ,start_delta, length_delta)
    return (name, shift)
