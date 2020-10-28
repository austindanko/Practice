from typing import Set

import requests
import pynmrstar

import time
time.sleep(.02)


known_good_values: Set[str] = set(requests.get('https://api.bmrb.io/v2/enumerations/_Experiment.Name').json()['values'])
lst_k_g_v = list(known_good_values)

all_entries = pynmrstar.utils.iter_entries()
experiments = set()
for entry in all_entries:
    value = entry.get_tag('_Experiment.Name')
    experiments.update(value)
lst_experiments = list(experiments)

odd_balls = []

for x in lst_experiments:
    if x not in lst_k_g_v:
        odd_balls.append(x)

exp_dict = {x:odd_balls.count(x)
          for x in odd_balls[:10]}
srt_dict = sorted(exp_dict.items(), key=lambda x:
                  x[1], reverse=True)
for x in srt_dict:
    print(x[0], x[1])



