from typing import Set, Dict, Iterable, List
import csv
import requests
import pynmrstar
import time

known_good_values: Set[str] = set(requests.get('https://api.bmrb.io/v2/enumerations/_Experiment.Name').json()['values'])
dict_k_g_v: Dict[str, bool] = {x: True for x in known_good_values}



all_entries: Iterable[pynmrstar.Entry] = pynmrstar.utils.iter_entries()
experiments: Set[str] = set([])
for entry in all_entries:
    value = entry.get_tag('_Experiment.Name')
    experiments.update(value)
    time.sleep(.03)

lst_experiments: List[str] = list(experiments)

odd_balls: List[str] = []

for x in lst_experiments:
    if x not in dict_k_g_v:
        odd_balls.append(x)

exp_dict: Dict[str, bool] = {}

for item in odd_balls:
    if item not in exp_dict:
        exp_dict[item] = 1
    else:
        exp_dict[item] += 1

exp_dict: Dict[str, bool] = {x:odd_balls.count(x)
          for x in odd_balls}
srt_dict = sorted(exp_dict.items(), key=lambda x:
                  x[1], reverse=True)
for x in srt_dict:
    print(x[0], x[1])



