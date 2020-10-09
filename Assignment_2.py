#Create a loop for _Experiment.Names, and save each one to a SET

import pynmrstar

all_entries = pynmrstar.utils.iter_entries()

experiments = set()

for entry in all_entries:
    value = entry.get_tag('_Experiment.Name')
    experiments.update(value)

for title in experiments:
    print(title)





