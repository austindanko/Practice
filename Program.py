import operator
import os
from typing import Set, Dict, Iterable, List, Tuple, Union, Generator, Any
import csv
import requests
import pynmrstar
from strsimpy.jaro_winkler import JaroWinkler

experiments: List[str] = []
lst_experiments: List[str] = list(experiments)
known_good_values: Set[str] = set(requests.get('https://api.bmrb.io/v2/enumerations/_Experiment.Name').json()['values'])


def get_obscur():
    obscurities: List[str] = []
    obscurity_count: Dict[str, bool] = {x: obscurities.count(x) for x in obscurities}
    for obscurity in lst_experiments:
        if obscurity not in known_good_values and obscurity not in pynmrstar.definitions.NULL_VALUES:
            obscurities.append(obscurity)
    for obscurity in set(sorted(obscurities)):
        sim_val: List[Tuple[str, float]] = []
        for good_value in known_good_values:
            similarity_value: float = jaro(obscurity, good_value)
            sim_val.append((good_value, similarity_value))
            sim_val.sort(reverse=True, key=operator.itemgetter(1))
        topthree: List[Union[str, float, int]] = []
        topthree.extend([x for y in sim_val[:3] for x in y])
        output = [obscurity, obscurity_count[obscurity]] + topthree

        if obscurity_count[obscurity] <= 10:
            csv_writer_b.writerow(output)
        else:
            csv_writer_a.writerow(output)


def existence():
    all_entries: Iterable[pynmrstar.Entry] = pynmrstar.utils.iter_entries()
    jaro = JaroWinkler().similarity
    mapping: Dict[str, Any] = {'api.bmrb': all_entries, 'jaro_sim': jaro}

    for algorithm in mapping:
        print(f'Running {algorithm}...')
        if os.path.exists(f'{algorithm}.csv') and f'{algorithm}' == 'api.bmrb':
            with open('api.bmrb.csv', 'r') as file:
                csv_reader = csv.reader(file)
                lst_experiments = next(csv_reader)
        elif not os.path.exists (f'{algorithm}.csv') and f'{algorithm}' == 'api.bmrb':
            for entry in all_entries:
                value = entry.get_tag('_Experiment.Name')
                experiments.extend(value)
            with open('api.bmrb.csv', 'w') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(lst_experiments)
        elif os.path.exists(f'{algorithm}.csv') and f'{algorithm}' == 'jaro.sim':
            pass
        elif not os.path.exists (f'{algorithm}.csv') and f'{algorithm}' == 'jaro.sim':
            with open('jaro_sim.csv', 'w') as file_a, open('jaro_sim_orphan.csv', 'w') as file_b:
                csv_writer_a = csv.writer(file_a)
                csv_writer_b = csv.writer(file_b)
                fields: List[str] = ['Obscurity', 'Count', 'KGV1', 'Similarity1',
                                     'KGV2', 'Similarity2', 'KGV3', 'Similarity3']
                csv_writer_a.writerow(fields)
                csv_writer_b.writerow(fields)
                get_obscur()

existence()


