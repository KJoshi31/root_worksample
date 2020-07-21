import datetime


class Driver:
    def __init__(self, name):
        self.name = name
        self.trips = list()

    def add_trip(self, trip):
        if not isinstance(trip, Trip):
            raise Exception('is not a valid Trip object')

        self.trips.append(trip)

    def get_trips(self):
        return self.trips

    def get_trip_totals(self):

        total_mins = 0
        total_miles = 0
        for trip in self.trips:
            total_mins = total_mins + trip.get_time_minutes()
            total_miles = total_miles + trip.distance

        return total_miles, total_mins


class Trip:

    def __init__(self, start_time, end_time, distance):
        self.start_time = self.get_time_as_datetime(start_time)
        self.end_time = self.get_time_as_datetime(end_time)
        self.distance = self.convert_dist_to_flt(distance)

    @classmethod
    def get_time_as_datetime(cls, time_str):
        try:
            date_obj = datetime.datetime.strptime(time_str, '%H:%M')
        except:
            raise Exception('time string is not correct format')

        return date_obj

    def get_time_minutes(self):
        start_date_obj = self.start_time
        end_date_obj = self.end_time
        minutes = (end_date_obj-start_date_obj).total_seconds() / 60.0
        return minutes

    @classmethod
    def convert_dist_to_flt(cls, distance):
        try:
            float_distance = float(distance)
        except:
            raise Exception('distance is not correct format')

        return float_distance