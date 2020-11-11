from typing import Set, Dict, Iterable, List
import csv
import requests
import pynmrstar
import time

import strsimpy as strsimpy
from strsimpy.jaro_winkler import JaroWinkler

lst1 = ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz')
lst2 = ('abc', 'xxx', 'xxx', 'jkl', 'xxx', 'pqq', 'stu', 'vwv', 'yz')
outsiders = ()
jaro = JaroWinkler()

for x, y in zip(lst1, lst2):
    if jaro.similarity(x, y) <= .5:
        print(x, y)
    else:
        print("No Match")


#    with open('api.bmrb.csv', 'w') as f:
#        w = csv.writer(f)
#        w.writerows($$$$$.items())
#
#with open('api_bmrb.csv') as f:
#    r = csv.reader(f)
#    $$$$$ = {row[0]: row[1] for row in r}


#if not os.path.exists('api.bmrb.csv'):


