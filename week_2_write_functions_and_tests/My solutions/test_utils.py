from utils import (surface_of_square,check_prime_number,is_leap, calculate_age_in_days,nearest_square,taxi_fares)
from unittest import mock
from datetime  import date
import pytest


@pytest.mark.parametrize("test_input,expected", [(5, 25), (9, 81), (5.5, 30.25)])
def test_surface_of_square(test_input, expected):
    assert surface_of_square(test_input)==expected

@pytest.mark.parametrize("test_input,expected", [(5, True), (1, False), (11, True), (8, False)])
def test_check_prime_number(test_input, expected):
    assert check_prime_number(test_input)==expected
    
@pytest.mark.parametrize("test_input,expected", [(2000, True), (2100, False), (2400, True), (2500, False), (3455, False)])
def test_is_leap(test_input, expected):
    assert is_leap(test_input)==expected

@pytest.mark.parametrize("test_input,expected", [('1989/04/15', '11478 days'), ('2002/02/02', '6802 days')])    
def test_calculate_age_in_days(test_input, expected):    
    with mock.patch('utils.get_today', return_value=date(2020, 9, 17)):
        res = calculate_age_in_days(birthdate=test_input)
        assert res == expected

@pytest.mark.parametrize("test_input,expected", [(107, 100), (1, 1),(2, 1), (3, 4), (-30, 0)])         
def test_nearest_square(test_input, expected):
    assert nearest_square(test_input)==expected
    
@pytest.mark.parametrize("test_input,expected", [(100, 182.57), (2, 7.57)])     
def test_taxi_fares(test_input, expected):
    assert taxi_fares(test_input)==expected
