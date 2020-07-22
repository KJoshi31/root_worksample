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
        report_engine = ReportEngine()
        report_engine.object_loader(default_correct_input)
        return report_engine

    @pytest.fixture
    def report_engine_only_drivers(self, only_drivers_input):
        report_engine = ReportEngine()
        report_engine.object_loader(only_drivers_input)
        return report_engine

    @pytest.fixture
    def report_engine_only_trips(self, only_trips_input):
        report_engine = ReportEngine()
        report_engine.object_loader(only_trips_input)
        return report_engine

    def test_create_report_engine(self, create_report_engine):
        new_re = create_report_engine
        assert isinstance(new_re, ReportEngine) == True

    def test_get_object_data_empty(self, create_report_engine):
        new_re = create_report_engine
        obj_data = new_re.get_object_data()
        assert type(obj_data) == dict
        assert len(obj_data.keys()) == 0

    def test_report_engine_default_obj_data(self, report_engine_default_obj_data, default_correct_input):
        new_re = report_engine_default_obj_data
        obj_data = new_re.get_object_data()

        assert(len(obj_data.keys())) == len(default_correct_input) - 3

    def test_report_engine_only_drivers(self, report_engine_only_drivers, only_drivers_input):
        new_re = report_engine_only_drivers
        obj_data = new_re.get_object_data()

        assert(len(obj_data.keys())) == len(only_drivers_input)

    def test_report_engine_only_trips(self, report_engine_only_trips, only_trips_input):
        new_re = report_engine_only_trips
        obj_data = new_re.get_object_data()

        assert(len(obj_data.keys())) == 0

    def test_default_obj_list_by_mile_order(self, report_engine_default_obj_data):
        sorted_list = report_engine_default_obj_data.get_drivers_list_by_mile_total()
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
        driver_data_list = report_engine_default_obj_data.get_drivers_list_by_mile_total()
        flattened_driver_data = report_engine_default_obj_data.get_flat_data_hash_list(driver_data_list)

        assert type(flattened_driver_data) == list

        for data_dict in flattened_driver_data:
            assert type(data_dict) == dict
            
            keys = data_dict.keys()
            for key in keys:
                assert 'name' in keys
                assert 'miles' in keys
                assert 'mph' in keys

