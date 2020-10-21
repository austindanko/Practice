
lst = ["e1", "e1", "e1", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]

exp_dict = {x:lst.count(x)
            for x in lst[:5]}
print(exp_dict)

import pynmrstar

all_entries = pynmrstar.utils.iter_entries()

experiments = set()

for entry in all_entries:
    value = entry.get_tag('_Experiment.Name')
    experiments.update(value)

exp_dict_2 = {x:experiments.count(x)
              for x in experiments[:10]}
print(exp_dict_2)


