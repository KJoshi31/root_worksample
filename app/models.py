import datetime

class Driver:
    def __init__(self, name):
        self.name = name
        self.trips = list()

    def add_trip(self, trip):
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
        self.start_time = (start_time)
        self.end_time = (end_time)
        self.distance = self.convert_dist_to_flt(distance)

    def get_time_as_datetime(self, time_str):
        date_obj =datetime.datetime.strptime(time_str, '%H:%M')
        return date_obj

    def get_time_minutes(self):
        start_date_obj = self.get_time_as_datetime(self.start_time)
        end_date_obj = self.get_time_as_datetime(self.end_time)

        minutes = (end_date_obj-start_date_obj).total_seconds() / 60.0
        return minutes

    def get_trip_mph(self):
        mins = self.get_time_minutes()
        mph = (self.distance / mins) * 60
        return mph

    def convert_dist_to_flt(cls, distance):
        return float(distance)