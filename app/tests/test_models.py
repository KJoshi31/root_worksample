import pytest
from models import Driver, Trip

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

    def test_create_driver(self, create_driver):
        d = create_driver
        assert type(d) == Driver
        assert d.name == 'test'

    def test_create_driver_empty_trip(self, create_driver):
        d = create_driver
        trips = d.get_trips()
        assert type(trips) == list
        assert len(trips) == 0

    def test_create_driver_with_trips(self, create_driver,create_driver_with_trips):
        d = create_driver_with_trips
        trips = d.get_trips()
        assert d == create_driver
        assert type(d) == Driver
        assert len(trips) == 1


class TestTrip:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert x == 'hello'