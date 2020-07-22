from models import Driver, Trip
from consts import DRIVER, TRIP


class ReportEngine:
    """
        report_engine.py is used for loading data from the input file
        and transforming it into data structures & objects that
        may be used for calculations & manipulation. Output from this
        object results in a report string returned to the consumer.
    """

    def __init__(self):
        """
            constructor creates an empty dictionary
            that is later injected data with and used for 
            data manipulation upon.
        """
        self.object_data = dict()

    def get_object_data(self):
        """
            returns the object data diction member of this class.
        """
        return self.object_data

    def object_loader(self, input_data):
        """
            parses through the input data
            and loads it into the object data member 
            of this report engine class. Creates
            a dictionary where the key is a driver object
            and the value is a list of trips associated 
            with the driver. 
        """

        # two lists created for categorizing the input types
        driver_list = list()
        trip_list = list()

        # iterate through the inputs
        for input in input_data:
            input_words = input.split()

            # checks if the input command is driver or trip
            # puts the command in the respective bucket
            if input_words[0].lower().capitalize() == DRIVER:
                driver_list.append(input)
            elif input_words[0].lower().capitalize() == TRIP:
                trip_list.append(input)

        # iterate through the driver command list
        # and make it a key for the object data
        for driver_text in driver_list:
            driver_data = driver_text.split()
            driver_name = driver_data[1]

            # create list of driver names for checking if name is in list
            drive_obj_names = [driver.name for driver,
                               trip_list in self.object_data.items()]

            # if the driver name is not in the list, create a new key as the Driver object
            if driver_name not in drive_obj_names:
                new_driver = Driver(driver_name)
                self.object_data[new_driver] = list()

        # iterate through the trip commands
        for trip_text in trip_list:
            trip_data = trip_text.split()
            text_trip_driver = trip_data[1]
            text_start_time = trip_data[2]
            text_end_time = trip_data[3]
            text_distance = trip_data[4]

            # create a new Trip object
            new_trip = Trip(text_start_time, text_end_time, text_distance)

            # iterate through object_data for checking on the name
            for key, value in self.object_data.items():

                # if the driver name and trip driver is the same
                # append to the list of the trips for the object_data
                if key.name == text_trip_driver:
                    self.object_data[key].append(new_trip)

        # final iteration where the trips are added as children to the
        # actual driver objects instead of just in the object_data structure
        for driver_obj, trip_list in self.object_data.items():

            for trip in trip_list:
                driver_obj.add_trip(trip)

    def generate_report(self):
        """
            returns a string that is a formated 
            representation of the report output.
        """
        # requests the list of drivers that is ordered by mile total
        driver_data_list = self.get_drivers_list_by_mile_total()

        # we pass that list of drivers into this function to get the flattened data
        # this flattened data list of dictionaries is used for output
        flattened_driver_data = self.get_flat_data_hash_list(driver_data_list)

        report_str = ""

        for driver_data in flattened_driver_data:

            report_str = report_str + driver_data['name'] + ':'

            # if the mileage is greater than 0 and the mpg is greater than 0
            # then we add the mph string
            if driver_data['miles'] > 0 and driver_data['mph'] > 0:
                report_str += '\t' + str(driver_data['miles'])
                report_str += ' miles' + ' @ '
                report_str += str(driver_data['mph']) + ' mph'
                report_str += '\n'

            # otherwise, just output the miles
            else:
                report_str += '\t' + str(0)
                report_str += ' miles'
                report_str += '\n'

        return report_str

    def get_drivers_list_by_mile_total(self):
        """
            returns a list of drivers objects by the miles total.
            Operates on the object_data structure and does sorting
            based on the mileage and constructs a list of driver
            in order based on mileage total from greatest to least.
        """

        # create new dictionary and copy the object_data for manipulation
        mile_dict = dict()
        mile_dict = dict.copy(self.object_data)

        # iteration over the objects in the object_data structure
        for driver_obj, trip_list in mile_dict.items():
            miles, mins = driver_obj.get_trip_totals()

            # replace list of trips with the total miles for sorting
            mile_dict[driver_obj] = miles

        # sort the dictionary by the miles, which is the value
        sorted_rank = {k: v for k, v in sorted(
            mile_dict.items(), key=lambda item: item[1], reverse=True)}

        # create a list of the drivers to be returned
        # the list is created by the sorted rank dictionary
        sorted_list = [driver for driver, mile in sorted_rank.items()]

        return sorted_list

    def get_flat_data_hash_list(self, sorted_driver_list):
        """
            returns a list of dictionaries of the data
            from the passed in list of Drivers. 
            This function constructs dictionaries of data instead
            referencing objects.
        """
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
