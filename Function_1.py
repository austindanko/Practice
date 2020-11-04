import os
from typing import Set, Dict, Iterable, List
import csv
import requests
import pynmrstar
import time
import strsimpy as strsimpy
from strsimpy.jaro_winkler import JaroWinkler



known_good_values: Set[str] = set(requests.get('https://api.bmrb.io/v2/enumerations/_Experiment.Name').json()['values'])
dict_kgv: Dict[str, bool] = {x: True for x in known_good_values}

if not os.path.exists('api.bmrb.csv'):

    all_entries: Iterable[pynmrstar.Entry] = pynmrstar.utils.iter_entries()
    experiments: Set[str] = set([])

for entry in all_entries:
    value = entry.get_tag('_Experiment.Name')
    experiments.update(value)
    time.sleep(.03)
lst_experiments: List[str] = list(experiments)

with open('api.bmrb.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(lst_experiments.items())

with open('api_bmrb.csv') as f:
    r = csv.reader(f)
    experiments_csv = {row for row in r}

odd_balls: List[str] = []

for x in lst_experiments:
    if x not in dict_kgv:
        odd_balls.append(x)

exp_dict: Dict[str, bool] = {x: odd_balls.count(x)
                             for x in odd_balls}
srt_dict = sorted(exp_dict.items(), key=lambda x:
x[1], reverse=True)

jaro = JaroWinkler()

for x, y in zip(dict_kgv, odd_balls):
    if jaro.similarity(x, y) <= .5:
        print(x, y)
    else:
        print("No Match")
