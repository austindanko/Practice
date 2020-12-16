import operator
import os
from typing import Set, Dict, Iterable, List, Tuple, Union, Generator, Any
import csv
import requests
import pynmrstar
from strsimpy.jaro_winkler import JaroWinkler
from strsimpy.ngram import NGram
from strsimpy import SIFT4

known_good_values: Set[str] = set(requests.get('https://api.bmrb.io/v2/enumerations/_Experiment.Name').json()['values'])

if not os.path.exists('api.bmrb.csv'):
    all_entries: Iterable[pynmrstar.Entry] = pynmrstar.utils.iter_entries()
    experiments: List[str] = []
    for entry in all_entries:
        value = entry.get_tag('_Experiment.Name')
        experiments.extend(value)

    lst_experiments: List[str] = list(experiments)

    with open('api.bmrb.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(lst_experiments)
else:
    with open('api.bmrb.csv', 'r') as file:
        csv_reader = csv.reader(file)
        lst_experiments = next(csv_reader)

obscurities: List[str] = []

for obscurity in lst_experiments:
    if obscurity not in known_good_values:
        obscurities.append(obscurity)

#####
obscurity_count: Dict[str, bool] = {x: obscurities.count(x) for x in obscurities}
#####

jaro = JaroWinkler().similarity
sift = SIFT4().distance
threegram = NGram(3).distance

mapping = {'jaro': jaro, 'sift': sift, 'threegram': threegram}

for algorithm in mapping:
    print(f'Running {algorithm}...')
    with open(f'{algorithm}_sim.csv', 'w') as file:
        csv_writer = csv.writer(file)
        fields: List[str] = ['Obscurity', 'Count', 'KGV1', 'Similarity1', 'KDV2', 'Similarity2', 'KDV3', 'Similarity3']
        csv_writer.writerow(fields)
        for obscurity in obscurities:
            sim_val: List[Tuple[str, str, float]] = []
            for good_value in known_good_values:
                similarity_value: float = mapping[algorithm](obscurity, good_value)
                sim_val.append((obscurity, good_value, similarity_value))
            sim_val.sort(reverse=True, key=operator.itemgetter(0, 2))

            topthree: List[Union[str, float, int]] = []
            topthree.extend([x for y in sim_val[:3] for x in y])
            topthree.insert(1, obscurity_count[obscurity])
            topthree.pop(4)
            topthree.pop(6)
            csv_writer.writerow(topthree)
