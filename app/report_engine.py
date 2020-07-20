from models import Driver, Trip
from consts import DRIVER, TRIP


class ReportEngine:

    def __init__(self):
        self.object_data = dict()

    def get_object_data(self):
        return self.object_data

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

        for trip_text in trip_list:
            trip_data = trip_text.split()
            text_trip_driver = trip_data[1]
            text_start_time = trip_data[2]
            text_end_time = trip_data[3]
            text_distance = trip_data[4]

            new_trip = Trip(text_start_time, text_end_time, text_distance)
            # print(new_trip.start_time, new_trip.end_time, new_trip.distance)

            for key, value in self.object_data.items():

                if key.name == text_trip_driver:
                    self.object_data[key].append(new_trip)

        for driver_obj, trip_list in self.object_data.items():

            for trip in trip_list:
                driver_obj.add_trip(trip)

    def generate_report(self):

        driver_data_list = self.get_drivers_list_by_mile_total()
        flattened_driver_data = self.get_flat_data_hash_list(driver_data_list)

        report_str = ""

        for driver_data in flattened_driver_data:

            report_str = report_str + driver_data['name'] + ':'

            if driver_data['miles'] > 0 and driver_data['mph'] > 0:
                report_str += '\t' + str(driver_data['miles'])
                report_str += ' miles' + ' @ '
                report_str += str(driver_data['mph']) + ' mph'
                report_str += '\n'
            else:
                report_str += '\t' + str(0)
                report_str += ' miles'
                report_str += '\n'

        return report_str

    def get_drivers_list_by_mile_total(self):
        mile_dict = dict()
        for driver_obj, trip_list in self.object_data.items():

            if driver_obj.name not in mile_dict:
                mile_dict[driver_obj] = None

            miles, mins = driver_obj.get_trip_totals()
            mile_dict[driver_obj] = miles

        sorted_rank = {k: v for k, v in sorted(
            mile_dict.items(), key=lambda item: item[1], reverse=True)}
        sorted_list = [driver for driver, mile in sorted_rank.items()]

        return sorted_list

    def get_flat_data_hash_list(self, sorted_driver_list):

        flat_data_hash_list = list()
        for driver in sorted_driver_list:
            temp_dict = dict()

            miles, mins = driver.get_trip_totals()

            temp_dict['name'] = driver.name
            temp_dict['miles'] = round(miles)

            if miles > 0:
                temp_dict['mph'] = round((miles/mins) * 60)
            else:
                temp_dict['mph'] = 0
            flat_data_hash_list.append(temp_dict)

        return flat_data_hash_list
