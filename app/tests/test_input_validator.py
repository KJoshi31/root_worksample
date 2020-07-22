import pytest
from input_validator import argument_validator


@pytest.fixture
def default_correct_input():
    input_str = 'Driver Dan\nDriver Lauren\nDriver Kumi\n' +\
        'Trip Dan 07:15 07:45 17.3\nTrip Dan 06:12 06:32 21.8\nTrip Lauren 12:01 13:16 42.0'

    return input_str


@pytest.fixture
def empty_input():
    input_str = ""

    return input_str


@pytest.fixture
def only_drivers_input():
    input_str = 'Driver Dan\nDriver Lauren\nDriver Kumi'

    return input_str


@pytest.fixture
def only_trips_input():
    input_str = 'Trip Dan 07:15 07:45 17.3\nTrip Dan 06:12 06:32 21.8\nTrip Lauren 12:01 13:16 42.0'

    return input_str


def test_correct_input(default_correct_input):
    assert argument_validator(default_correct_input) == True


def test_empty_input(empty_input):
    with pytest.raises(Exception) as e:
        argument_validator(empty_input) == False


def test_only_drivers_input(only_drivers_input):
    assert argument_validator(only_drivers_input) == True


def test_only_trips_input(only_trips_input):
    assert argument_validator(only_trips_input) == True
