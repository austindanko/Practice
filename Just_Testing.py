from typing import Set, Dict, Iterable, List
import csv
import requests
import pynmrstar
import time

import strsimpy as strsimpy
from strsimpy.jaro_winkler import JaroWinkler

lst1 = ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz')
lst2 = ('abc', 'xxx', 'xxx', 'jkl', 'xxx', 'pqq', 'stu', 'vwv', 'yz')

jaro = JaroWinkler()

for x, y in zip(lst1, lst2):
    if jaro.similarity(x, y) <= .5:
        print(x, y)
    else:
        print("No Match")





