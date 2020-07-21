import pytest
from models import Driver, Trip
import datetime


class TestDriver:

    @pytest.fixture
    def create_driver(self):
        return Driver('test')

    @pytest.fixture
    def create_driver_with_trips(self, create_driver):
        d = create_driver
        t = Trip('01:00', '02:00', '17.3')
        d.add_trip(t)
        return d

    @pytest.fixture
    def driver_multiple_trips(self, create_driver_with_trips):
        d = create_driver_with_trips
        t = Trip('02:00', '15:00', '50')
        d.add_trip(t)
        return d

    def test_create_driver(self, create_driver):
        d = create_driver
        assert type(d) == Driver
        assert d.name == 'test'

    def test_create_driver_empty_trip(self, create_driver):
        d = create_driver
        trips = d.get_trips()
        assert type(trips) == list
        assert len(trips) == 0

    def test_create_driver_with_trips(self, create_driver, create_driver_with_trips):
        d = create_driver_with_trips
        trips = d.get_trips()
        assert d == create_driver
        assert type(d) == Driver
        assert len(trips) == 1

    def test_create_driver_with_invalid_trip(self, create_driver):
        d = create_driver
        t = "lkl"
        with pytest.raises(Exception) as e:
            d.add_trip(t)

    def test_get_trip_totals_single_trip(self, create_driver_with_trips):
        d = create_driver_with_trips
        miles, minutes = d.get_trip_totals()

        assert miles == 17.3
        assert minutes == 60

    def test_driver_multiple_trips(self, driver_multiple_trips):
        d = driver_multiple_trips
        miles, minutes = d.get_trip_totals()

        assert miles == 67.3
        assert minutes == 840


class TestTrip:
    @pytest.fixture
    def create_trip(self):
        t = Trip('01:00', '02:00', '10.1')
        return t

    def test_create_trip(self, create_trip):
        t = create_trip
        assert isinstance(t, Trip) == True
        assert isinstance(t.start_time, datetime.datetime)
        assert isinstance(t.end_time, datetime.datetime)
        assert type(t.distance) == float

    def test_get_time_as_datetime(self):
        time_string = "01:00"
        date_obj = Trip.get_time_as_datetime(time_string)
        assert isinstance(date_obj, datetime.datetime)

    def test_get_time_minutes(self, create_trip):
        t = create_trip
        mins = t.get_time_minutes()
        assert mins == 60

    def test_convert_dist_to_flt(self):
        dist_string = "35.5"
        distance_flt = Trip.convert_dist_to_flt(dist_string)
        assert type(distance_flt) == float
