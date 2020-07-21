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
