from models import Driver, Trip
from consts import DRIVER, TRIP

class ReportEngine:
    

    def __init__(self):
        self.object_data = dict()

    def get_object_data(self):
        return self.object_data
    
    def print_object_data(self):

            rep_str = ""

            for key,value in self.object_data.items():
                rep_str = rep_str+key.name + '\n'
                
                for item in value:
                    rep_str=rep_str+ '\t' + str(item.start_time)
                    rep_str=rep_str+ '\t' + str(item.end_time)
                    rep_str=rep_str+ '\t' + str(item.distance)+'\n'

            print(rep_str)


    def object_loader(self, input_data):
        driver_list = list()
        trip_list = list()

        for input in input_data:
            input_words = input.split()

            if input_words[0].lower().capitalize() == DRIVER:
                driver_list.append(input)
            elif input_words[0].lower().capitalize() == TRIP:
                trip_list.append(input)

        
        for driver_text in driver_list:
            driver_data = driver_text.split()
            driver_name = driver_data[1]

            if driver_name not in self.object_data:
                new_driver = Driver(driver_name)
                self.object_data[new_driver] = list()

        # print(self.object_data)

        for trip_text in trip_list:
            trip_data = trip_text.split()
            text_trip_driver = trip_data[1]
            text_start_time = trip_data[2]
            text_end_time = trip_data[3]
            text_distance = trip_data[4]

            new_trip = Trip(text_start_time, text_end_time, text_distance)
            # print(new_trip.start_time, new_trip.end_time, new_trip.distance)

            for key,value in self.object_data.items():

                if key.name == text_trip_driver:
                    self.object_data[key].append(new_trip)


    def generate_report(self):
        print(self.object_data)

        for driver_obj, trip_list in self.object_data.items():
            print(driver_obj.name)

            driver_obj.get_trip_totals()
                


