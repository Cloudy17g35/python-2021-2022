#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję char_sum, która dla zadanego łańcucha zwraca
sumę kodów ASCII znaków. Wykorzystaj funkcję ord()
"""

def char_sum(text):
    return sum([ord(char) for char in text])

input = "this is a string"
output = 1516

