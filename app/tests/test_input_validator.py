import pytest
from input_validator import argument_validator

def test_empty_contents():
    assert argument_validator([]) == False