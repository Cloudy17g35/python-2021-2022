#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Zad 2. Napisz funkcję even_elements zwracającą listę,
która zawiera tylko elementy z list o parzystych indeksach.
"""

def even_elements(lista):

    return [lista[i] for i in range(len(lista)) if i % 2 == 0]


input = [1, 2, 3, 4, 5, 6]
output = [1, 3, 5]
