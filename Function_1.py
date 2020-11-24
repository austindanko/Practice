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

    with open('api.bmrb.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(lst_experiments)
else:
    with open('api.bmrb.csv', 'r') as file:
        csv_reader = csv.reader(file)
        lst_experiments = next(csv_reader)

odd_balls: List[str] = []

for x in lst_experiments:
    if x not in dict_kgv:
        odd_balls.append(x)

exp_dict: Dict[str, bool] = {x: odd_balls.count(x) for x in odd_balls}
srt_dict = sorted(exp_dict.items(), key=lambda x: x[1], reverse=True)

jaro = JaroWinkler()

fields: List[str] = ['Known Good Values', 'Odd Balls', 'Similarity Value']

with open('similarity.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(fields)
    for x in dict_kgv:
        sim_val: List[str] = []
        for y in odd_balls:
            similarity_value: float = jaro.similarity(x, y)
            sim_val.append((y, similarity_value))
            csv_writer.writerow([x, y, similarity_value])
        sim_val.sort(reverse=True, key=lambda x: x[1])
        print(sim_val[:3])
