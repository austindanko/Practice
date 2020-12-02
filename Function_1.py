import operator
import os
from typing import Set, Dict, Iterable, List
import csv
import requests
import pynmrstar
import time
from strsimpy.jaro_winkler import JaroWinkler
from strsimpy.levenshtein import Levenshtein
from strsimpy.damerau import Damerau
from strsimpy.longest_common_subsequence import LongestCommonSubsequence
from strsimpy import SIFT4

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

Obscurity: List[str] = []

for x in lst_experiments:
    if x not in dict_kgv:
        Obscurity.append(x)

#####
exp_dict: Dict[str, bool] = {x: Obscurity.count(x) for x in Obscurity}
srt_dict = sorted(exp_dict.items(), key=lambda x: x[1], reverse=True)
#####

jaro = JaroWinkler()
leven = Levenshtein()
damerau = Damerau()
lcs = LongestCommonSubsequence()
sift = SIFT4()


with open('jaro_sim.csv', 'w') as file:
    csv_writer = csv.writer(file)
    fields: List[str] = ['Top Three Matching Obscurities']
    #csv_writer.writerow(fields)
    sim_val: List[str] = []
    for x in known_good_values:
        for y in exp_dict:
            similarity_value: float = jaro.similarity(x, y)
            sim_val.append((((("Known Good Value", x, "Obscurity", y, "Similarity", similarity_value)))))
    sim_val.sort(reverse=True, key=operator.itemgetter(1, 5))
# figure out a list of the top three matches of each known good value?

    for x in top_3:
        csv_writer.writerow(x)

#with open('lcs_sim.csv', 'w') as file:
#    csv_writer = csv.writer(file)
#    fields: List[str] = ['Top Three Matching Obscurities']
#    #csv_writer.writerow(fields)
#    sim_val: List[str] = []
#    for x in known_good_values:
#        for y in exp_dict:
#            similarity_value: float = lcs.distance(x, y)
#            sim_val.append((((("Known Good Value", x, "Obscurity", y, "Similarity", similarity_value)))))
#    sim_val.sort(reverse=True, key=operator.itemgetter(1, 5))
#
#    for x in sim_val:
#        csv_writer.writerow(x)
#
#with open('sift_sim.csv', 'w') as file:
#    csv_writer = csv.writer(file)
#    fields: List[str] = ['Top Three Matching Obscurities']
#    #csv_writer.writerow(fields)
#    sim_val: List[str] = []
#    for x in known_good_values:
#        for y in exp_dict:
#            similarity_value: float = sift.distance(x, y)
#            sim_val.append((((("Known Good Value", x, "Obscurity", y, "Similarity", similarity_value)))))
#    sim_val.sort(reverse=True, key=operator.itemgetter(1, 5))
#
#    for x in sim_val:
#        csv_writer.writerow(x)
#
#with open('leven_sim.csv', 'w') as file:
#    csv_writer = csv.writer(file)
#    fields: List[str] = ['Top Three Matching Obscurities']
#    #csv_writer.writerow(fields)
#    sim_val: List[str] = []
#    for x in known_good_values:
#        for y in exp_dict:
#            similarity_value: float = leven.distance(x, y)
#            sim_val.append((((("Known Good Value", x, "Obscurity", y, "Similarity", similarity_value)))))
#    sim_val.sort(reverse=True, key=operator.itemgetter(1, 5))
#
#    for x in sim_val:
#        csv_writer.writerow(x)
#
#with open('damerau_sim.csv', 'w') as file:
#    csv_writer = csv.writer(file)
#    fields: List[str] = ['Top Three Matching Obscurities']
#    #csv_writer.writerow(fields)
#    sim_val: List[str] = []
#    for x in known_good_values:
#        for y in exp_dict:
#            similarity_value: float = damerau.distance(x, y)
#            sim_val.append((((("Known Good Value", x, "Obscurity", y, "Similarity", similarity_value)))))
#    #sim_val.sort(reverse=True, key=lambda x: x[5])
#    sim_val.sort(reverse=True, key=operator.itemgetter(1, 5))
#
#    for x in sim_val:
#        csv_writer.writerow(x)



