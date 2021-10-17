#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Napisz funkcję days_in_year zwracającą liczbę dni w roku (365 albo 366).
"""

def is_leap(year: int) -> bool:

    """:argument year: type int type
        :returns bool True if year is leap False otherwise"""

    if year % 100 == 0 and year % 400:  # years divisible by 100 but not by 400 are not considered as leap
        return False
    elif year % 4 == 0:
        return True
    return False


def days_in_year(year):
    return 366 if is_leap(year) else 365
    

inputs = [2019, 2020, 2014, 2100, 2400]
outputs = [365, 366, 365, 365, 366]
