import os
from typing import Set, Dict, Iterable, List
import csv
import requests
import pynmrstar
import time
import strsimpy as strsimpy
from strsimpy.jaro_winkler import JaroWinkler

jaro = JaroWinkler()

lst1 = ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz')
lst2 = ('abc', 'xxx', 'xxx', 'jkl', 'xxx', 'pqq', 'stu', 'vwv', 'yz')
outsiders = ()

fields = ['Known Good Values', 'Odd Balls', 'Similarity Value']

with open('Fuck', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(fields)
    for x in lst1:
        for y in lst2:
            similarity_value: float = jaro.similarity(x, y)
            csv_writer.writerow([x, y, similarity_value])







