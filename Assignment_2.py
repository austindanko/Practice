import pynmrstar

entry15000 = pynmrstar.Entry.from_database(15000)

all_entries = pynmrstar.utils.iter_entries()


for entry in all_entries:
    value = entry.get_tag('_Experiment.Name')
    print(value)