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
    if obscurity not in known_good_values and obscurity not in pynmrstar.definitions.NULL_VALUES:
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
    with open(f'{algorithm}_sim.csv', 'w') as file_a, open(f'{algorithm}_sim_orphan.csv', 'w') as file_b:
        csv_writer_a = csv.writer(file_a)
        csv_writer_b = csv.writer(file_b)
        fields: List[str] = ['Obscurity', 'Count', 'KGV1', 'Similarity1', 'KGV2', 'Similarity2', 'KGV3', 'Similarity3']
        csv_writer_a.writerow(fields)
        csv_writer_b.writerow(fields)
        for obscurity in set(sorted(obscurities)):
            sim_val: List[Tuple[str, float]] = []
            for good_value in known_good_values:
                similarity_value: float = mapping[algorithm](obscurity, good_value)
                sim_val.append((good_value, similarity_value))

            if algorithm == 'jaro':
                sim_val.sort(reverse=True, key=operator.itemgetter(1))
            else:
                sim_val.sort(reverse=False, key=operator.itemgetter(1))

            topthree: List[Union[str, float, int]] = []
            topthree.extend([x for y in sim_val[:3] for x in y])
            output = [obscurity, obscurity_count[obscurity]] + topthree

            if obscurity_count[obscurity] <= 10:
                csv_writer_b.writerow(output)
            else:
                csv_writer_a.writerow(output)



