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
lst2 = ('abx', 'axbxc', 'xxbc', 'axbc', 'abc',
        'xef', 'dex', 'fed', 'exf', 'defx', 'def',
        'hixg', 'gxh', 'ghxi', 'xhx', 'ghix', 'ghi',
        'jxx', 'jkxlj', 'xkx', 'jkl',
        'mnxx', 'mxno', 'xmno', 'onm', 'mno',
        'pqx', 'pqqq', 'pqr', 'pqxrx', 'xqx',
        'stu', 'xtx', 'sxtu', 'xxu', 'stt',
        'vxxx', 'xxw', 'vwx', 'vwww', 'vwwx',
        'xyz', 'xxz', 'yz', 'yx', 'xxx', 'zyx')
outsiders: List[str] = []

fields: List[str] = ['Known Good Values', 'Odd Balls', 'Similarity Value']

with open('TestTestTest', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(fields)
    for x in lst1:
        #Create an object that stores the similarity value
        sim_val: List[str] = []
        # first element of the first list against every element of list 2, then on to the next element of list 1
        for y in lst2:
            # add the similarity value as well as y  between x and y elements, append to data structure
            similarity_value: float = jaro.similarity(x, y)
            sim_val.append((y, similarity_value))
            #similarity_value.sort(reverse = True)
            csv_writer.writerow([x, y, similarity_value])
        sim_val.sort(reverse=True, key=lambda x: x[1])
        print(sim_val[:3])

        # after all elements have ran, sort highest value to least
        # take top three of each element, utilize index x=[0:2]







