from data_model.shift import create_shift

class Individual(object):
    """docstring for Individual.
    This class contains all informations connected to individial person.
    Schedule list consists tuples of shifts"""
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule

    def add_shift(self, arg):
        pass

    def get_shifts(self, arg):
        pass

    def __repr__(self):
        return 'Individual("%s", schedules=%s)' % (self.name, len(self.schedule))
