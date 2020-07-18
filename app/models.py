

class Driver:
    def __init__(self, name):
        self.name = name
        self.trips = list()

    def add_trip(self, trip):
        self.trips.append(trip)


class Trip:
    
    def __init__(self, start_time, end_time, distance):
        self.start_time = self.convert_times_to_flt(start_time)
        self.end_time = self.convert_times_to_flt(end_time)
        self.distance = self.convert_dist_to_flt(distance)


    def convert_times_to_flt(cls, time):
        time_arr = time.split(':')
        new_time = time_arr[0]+'.'+time_arr[1]
        return float(new_time)

    def convert_dist_to_flt(cls, distance):
        return float(distance)