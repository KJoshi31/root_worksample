import datetime

"""
    models.py contains classes Driver and Trip, which are object
    representations of the data that is incoming from the input file.
"""


class Driver:
    """
        Driver class is a representation of driver data
        that comes from a driver command from the input file.
        Each driver has a list of Trips serving as a children.
    """

    def __init__(self, name):
        """
            construtor takes in name string and
            also initilizes empty string for Trips 
            that are associated with the Driver
        """
        self.name = name
        self.trips = list()

    def add_trip(self, trip):
        """
            takes an argument of trip.
            if it is not a Trip object type an exception is thrown.
            adds the trip item to the trips list, serviing as a child
            of the driver.
        """
        if not isinstance(trip, Trip):
            raise Exception('is not a valid Trip object')

        self.trips.append(trip)

    def get_trips(self):
        """
            returns list of trips associated with the driver.
        """
        return self.trips

    def get_trip_totals(self):
        """
            returns the total miles and minutes associated
            with the list of trip children for the driver.
            this is calculated in conjecture with the trip
            returing the time in minutes.
        """
        total_mins = 0
        total_miles = 0
        for trip in self.trips:
            total_mins = total_mins + trip.get_time_minutes()
            total_miles = total_miles + trip.distance

        return total_miles, total_mins


class Trip:
    """
        Trip class is a representation of trip data
        that comes from a trip command from the input file.
        Trip is considered a child of a Driver object.
    """

    def __init__(self, start_time, end_time, distance):
        """
            construtor takes in start_time,end_time,and distance
            arguments as strings. The start_time and end_times get
            converted to datetime objects and the distance gets 
            converted to a float.
        """
        self.start_time = self.get_time_as_datetime(start_time)
        self.end_time = self.get_time_as_datetime(end_time)
        self.distance = self.convert_dist_to_flt(distance)

    @classmethod
    def get_time_as_datetime(cls, time_str):
        """
            a string for time gets passed in and gets 
            converted to a datetime object. If its not
            a correct format of Hour and Minute, an exception 
            is thrown.
        """
        try:
            date_obj = datetime.datetime.strptime(time_str, '%H:%M')
        except:
            raise Exception('time string is not correct format')

        return date_obj

    def get_time_minutes(self):
        """
            returns the number of minutes
            from the difference between the start_time
            and end_time datetime objects.
        """
        start_date_obj = self.start_time
        end_date_obj = self.end_time
        minutes = (end_date_obj-start_date_obj).total_seconds() / 60.0
        return minutes

    @classmethod
    def convert_dist_to_flt(cls, distance):
        """
            a distance string gets passed in 
            and converted to a float, otherwise
            an exception is thrown if its not convertable.
        """
        try:
            float_distance = float(distance)
        except:
            raise Exception('distance is not correct format')

        return float_distance
