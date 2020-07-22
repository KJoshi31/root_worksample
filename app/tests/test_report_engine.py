import pytest
from report_engine import ReportEngine
from .test_input_validator import default_correct_input, only_drivers_input, only_trips_input


class TestReportEngine:

    @pytest.fixture
    def create_report_engine(self):
        report_engine = ReportEngine()
        return report_engine

    @pytest.fixture
    def report_engine_default_obj_data(self, default_correct_input):
        default_correct_list = default_correct_input.split('\n')
        report_engine = ReportEngine()
        report_engine.object_loader(default_correct_list)
        return report_engine, default_correct_list

    @pytest.fixture
    def report_engine_only_drivers(self, only_drivers_input):
        only_drivers_list = only_drivers_input.split('\n')
        report_engine = ReportEngine()
        report_engine.object_loader(only_drivers_list)
        return report_engine, only_drivers_list

    @pytest.fixture
    def report_engine_only_trips(self, only_trips_input):
        only_trip_list = only_trips_input.split('\n')
        report_engine = ReportEngine()
        report_engine.object_loader(only_trip_list)
        return report_engine, only_trip_list

    def test_create_report_engine(self, create_report_engine):
        new_re = create_report_engine
        assert isinstance(new_re, ReportEngine) == True

    def test_get_object_data_empty(self, create_report_engine):
        new_re = create_report_engine
        obj_data = new_re.get_object_data()
        assert type(obj_data) == dict
        assert len(obj_data.keys()) == 0

    def test_report_engine_default_obj_data(self, report_engine_default_obj_data):
        new_re, input_list = report_engine_default_obj_data
        obj_data = new_re.get_object_data()

        assert(len(obj_data.keys())) == len(input_list) - 3

    def test_report_engine_only_drivers(self, report_engine_only_drivers):
        new_re, only_drivers_list = report_engine_only_drivers
        obj_data = new_re.get_object_data()

        assert(len(obj_data.keys())) == len(only_drivers_list)

    def test_report_engine_only_trips(self, report_engine_only_trips):
        new_re, only_trip_list = report_engine_only_trips
        obj_data = new_re.get_object_data()

        assert(len(obj_data.keys())) == 0

    def test_default_obj_list_by_mile_order(self, report_engine_default_obj_data):
        sorted_list = report_engine_default_obj_data[0].get_drivers_list_by_mile_total(
        )
        driver1 = sorted_list[0]
        driver2 = sorted_list[1]
        driver3 = sorted_list[2]

        assert len(sorted_list) == 3
        assert driver1.name == 'Lauren'
        assert driver2.name == 'Dan'
        assert driver3.name == 'Kumi'
        assert driver1.get_trip_totals()[0] > driver2.get_trip_totals()[0]
        assert driver2.get_trip_totals()[0] > driver3.get_trip_totals()[0]
        assert driver1.get_trip_totals()[0] > driver3.get_trip_totals()[0]

    def test_default_obj_flat_data_hash_list(self, report_engine_default_obj_data):
        report_eng_obj, input_list = report_engine_default_obj_data
        driver_data_list = report_eng_obj.get_drivers_list_by_mile_total()
        flattened_driver_data = report_eng_obj.get_flat_data_hash_list(
            driver_data_list)

        assert type(flattened_driver_data) == list

        for data_dict in flattened_driver_data:
            assert type(data_dict) == dict

            keys = data_dict.keys()
            for key in keys:
                assert 'name' in keys
                assert 'miles' in keys
                assert 'mph' in keys

    def test_obj_list_by_mile_order_only_drivers(self, report_engine_only_drivers):
        sorted_list = report_engine_only_drivers[0].get_drivers_list_by_mile_total(
        )
        driver1 = sorted_list[0]
        driver2 = sorted_list[1]
        driver3 = sorted_list[2]

        assert len(sorted_list) == 3
        assert driver1.name == 'Dan'
        assert driver2.name == 'Lauren'
        assert driver3.name == 'Kumi'
        assert driver1.get_trip_totals()[0] == driver2.get_trip_totals()[0]
        assert driver2.get_trip_totals()[0] == driver3.get_trip_totals()[0]
        assert driver1.get_trip_totals()[0] == driver3.get_trip_totals()[0]

    def test_only_drivers_flat_data_hash_list(self, report_engine_only_drivers):
        report_eng_obj, input_list = report_engine_only_drivers
        driver_data_list = report_eng_obj.get_drivers_list_by_mile_total()
        flattened_driver_data = report_eng_obj.get_flat_data_hash_list(
            driver_data_list)

        assert type(flattened_driver_data) == list

        for data_dict in flattened_driver_data:
            assert type(data_dict) == dict

            keys = data_dict.keys()
            for key in keys:
                assert 'name' in keys
                assert 'miles' in keys
                assert 'mph' in keys

            if 'mph' in keys:
                assert data_dict['mph'] == 0
            if 'miles' in keys:
                assert data_dict['miles'] == 0

    def test_obj_list_by_mile_order_only_trips(self, report_engine_only_trips):
        sorted_list = report_engine_only_trips[0].get_drivers_list_by_mile_total(
        )

        assert len(sorted_list) == 0

    def test_only_trips_flat_data_hash_list(self, report_engine_only_trips):
        report_eng_obj, input_list = report_engine_only_trips
        driver_data_list = report_eng_obj.get_drivers_list_by_mile_total()
        flattened_driver_data = report_eng_obj.get_flat_data_hash_list(
            driver_data_list)

        assert type(flattened_driver_data) == list
        assert len(flattened_driver_data) == 0
