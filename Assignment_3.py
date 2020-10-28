from typing import Set

import requests
import pynmrstar

known_good_values: Set[str] = set(requests.get('https://api.bmrb.io/v2/enumerations/_Experiment.Name').json()['values'])

lst = ["e1", "e1", "e1", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]

exp_dict = {x:lst.count(x)
            for x in lst[:5]}
#print(exp_dict)

#import time
#time.sleep(.02)

all_entries = pynmrstar.utils.iter_entries()

for entry in all_entries:
    value = entry.get_tag('_Experiment.Name')
    exp_dict_2 = {x: value.count(x)
                  for x in value[:10]}
    print(exp_dict_2)





