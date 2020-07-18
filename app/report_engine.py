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

        for driver_obj, trip_list in self.object_data.items():

            for trip in trip_list:
                driver_obj.add_trip(trip)


    def generate_report(self):

        report_str = ""
        driver_data_list = self.get_flat_object_data()

        for driver_data in driver_data_list:

            report_str = report_str + driver_data['name'] + ':'

            if driver_data['miles']>0 and driver_data['mph']>0:
                report_str += '\t'+ str(driver_data['miles'])
                report_str += ' miles' + ' @ '
                report_str += str( driver_data['mph'] ) + ' mph'
                report_str += '\n'
            else:
                report_str += '\t'+ str(0)
                report_str += ' miles'
                report_str += '\n'


        return report_str

    def sort_object_data_transform(self):
        mile_dict = dict()
        for driver_obj, trip_list in self.object_data.items():
            
            if driver_obj.name not in mile_dict:
                mile_dict[driver_obj] = None
            
            miles, mins = driver_obj.get_trip_totals()
            mile_dict[driver_obj] = miles
        
        sorted_rank = {k: v for k, v in sorted(mile_dict.items(), key=lambda item: item[1], reverse=True)}

        return sorted_rank


    def get_flat_object_data(self): 
        sorted_rank = self.sort_object_data_transform()

        scrubbed_data = list()
        for driver_obj, miles in sorted_rank.items():
            temp_dict = dict()
            miles, mins = driver_obj.get_trip_totals()

            temp_dict['name'] = driver_obj.name
            temp_dict['miles'] = round(miles)
            if miles > 0:
                temp_dict['mph'] = round((miles/mins) * 60)
            else:
                temp_dict['mph'] = 0
            scrubbed_data.append(temp_dict)

        return scrubbed_data