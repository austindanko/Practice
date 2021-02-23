import operator
import os
from typing import Set, Dict, Iterable, List, Tuple, Union, Generator, Any
import csv
import requests
import pynmrstar
from strsimpy.jaro_winkler import JaroWinkler

known_good_values: Set[str] = set(requests.get('https://api.bmrb.io/v2/enumerations/_Experiment.Name').json()['values'])


def obscure(experiments: List[str]) -> List[str]:
    obscurities: List[str] = []
    for obscurity in experiments:
        if obscurity not in known_good_values and obscurity not in pynmrstar.definitions.NULL_VALUES:
            obscurities.append(obscurity)
    return obscurities


def experiment_sim(obscurities: List[str]) -> None:
    jaro = JaroWinkler().similarity
    obscurity_count: Dict[str, bool] = {x: obscurities.count(x) for x in obscurities}
    print('Running jaro...')
    with open('jaro_sim.csv', 'a') as file_jaro_sim:
        jaro_sim_writer = csv.writer(file_jaro_sim)
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
                    with open('jaro_sim_orphan.csv', 'a') as file_jaro_sim_orphan:
                        jaro_sim_orphan_writer = csv.writer(file_jaro_sim_orphan)
                        jaro_sim_orphan_writer.writerow(output)
                else:
                    jaro_sim_writer.writerow(output)


def existence() -> List[str]:
    pathway: List[str] = ['api', 'jaro']
    experiments: List[str] = []
    for path in pathway:
        if path == 'api':
            if os.path.exists('api.bmrb.csv'):
                with open('api.bmrb.csv', 'r') as file:
                    csv_reader = csv.reader(file)
                    experiments = next(csv_reader)
            else:
                all_entries: Iterable[pynmrstar.Entry] = pynmrstar.utils.iter_entries()
                print('Running api.bmrb...')
                for entry in all_entries:
                    value = entry.get_tag('_Experiment.Name')
                    experiments.extend(value)
                with open('api.bmrb.csv', 'w') as file_api_bmrb:
                    api_bmrb_writer = csv.writer(file_api_bmrb)
                    api_bmrb.writerow(experiments)
        elif path == 'jaro':
            if os.path.exists('jaro_sim.csv'):
                pass
                # paste function2 line 52 ->
            else:
                print('Running jaro...')
                with open('jaro_sim.csv', 'w') as file_jaro_sim, \
                        open('jaro_sim_orphan.csv', 'w') as file_jaro_sim_orphan:
                    csv_writer_a = csv.writer(file_jaro_sim)
                    csv_writer_b = csv.writer(file_jaro_sim_orphan)
                    fields: List[str] = ['Obscurity', 'Count', 'KGV1', 'Similarity1',
                                         'KGV2', 'Similarity2', 'KGV3', 'Similarity3']
                    csv_writer_a.writerow(fields)
                    csv_writer_b.writerow(fields)
    return experiments


experiment_sim(obscure(existence()))
