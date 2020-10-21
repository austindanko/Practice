
lst = ["e1", "e1", "e1", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]

exp_dict = {x:lst.count(x)
            for x in lst[:5]}
#print(exp_dict)

exp_set = set()
for x in lst:
    exp_set.update(lst)
#print(exp_set)

exp_dict_3 = {x:exp_set.count(x)
              for x in exp_set}
print(exp_dict_3)

#import pynmrstar

#all_entries = pynmrstar.utils.iter_entries()

#experiments = set()

#for entry in all_entries:
#    value = entry.get_tag('_Experiment.Name')
#    experiments.update(value)

#exp_dict_2 = {x:experiments.count(x)
#              for x in experiments[:10]}
#print(exp_dict_2)


