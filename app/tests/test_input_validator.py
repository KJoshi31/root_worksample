import pytest
from input_validator import argument_validator


@pytest.fixture
def default_correct_input():
    input_str = 'Driver Dan\nDriver Lauren\nDriver Kumi\n' +\
        'Trip Dan 07:15 07:45 17.3\nTrip Dan 06:12 06:32 21.8\nTrip Lauren 12:01 13:16 42.0'

    return input_str.split('\n')


def test_correct_input(default_correct_input):
    assert argument_validator(default_correct_input) == True


def test_empty_contents():
    assert argument_validator([]) == False
