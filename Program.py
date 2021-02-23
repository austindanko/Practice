import operator
import os
from typing import Set, Dict, Iterable, List, Tuple, Union, Generator, Any
import csv
import requests
import pynmrstar
from strsimpy.jaro_winkler import JaroWinkler

known_good_values: Set[str] = set(requests.get('https://api.bmrb.io/v2/enumerations/_Experiment.Name').json()['values'])





def obscure(lst_experiments: List[str]) -> List[str]:
    obscurities: List[str] = []
    for obscurity in lst_experiments:
        if obscurity not in known_good_values and obscurity not in pynmrstar.definitions.NULL_VALUES:
            obscurities.append(obscurity)
    return obscurities


def experiment_sim(obscurities: List[str]) -> None:
    jaro = JaroWinkler().similarity
    obscurity_count: Dict[str, bool] = {x: obscurities.count(x) for x in obscurities}
    print('Running jaro...')
    with open('jaro_sim.csv', 'r') as file_a, open('jaro_sim.csv', 'w') as file_b:
        csv_reader = csv.reader(file_a)
        csv_writer = csv.writer(file_b)
        csv_writer.writerow(next(csv_reader))
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
                    with open('jaro_sim_orphan.csv', 'r') as file_c, open('jaro_sim_orphan.csv', 'w') as file_d:
                        csv_reader = csv.reader(file_c)
                        csv_writer = csv.writer(file_d)
                        csv_writer.writerow(next(csv_reader))
                        csv_writer.writerow(output)
                else:
                    csv_writer.writerow(output)


def existence():
    pathway: List[str] = ['api', 'jaro']
    experiments: List[str] = []
    lst_experiments: List[str] = list(experiments)
    for path in pathway:
        if path == 'api':
            if os.path.exists('api.bmrb.csv'):
                with open('api.bmrb.csv', 'r') as file:
                    csv_reader = csv.reader(file)
                    lst_experiments = next(csv_reader)
            else:
                all_entries: Iterable[pynmrstar.Entry] = pynmrstar.utils.iter_entries()
                print('Running api.bmrb...')
                for entry in all_entries:
                    value = entry.get_tag('_Experiment.Name')
                    experiments.extend(value)
                with open('api.bmrb.csv', 'w') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(lst_experiments)
        elif path == 'jaro':
            if os.path.exists('jaro_sim.csv'):
                pass
                #paste function2 line 52 ->
            else:
                print('Running jaro...')
                with open('jaro_sim.csv', 'w') as file_a, open('jaro_sim_orphan.csv', 'w') as file_b:
                    csv_writer_a = csv.writer(file_a)
                    csv_writer_b = csv.writer(file_b)
                    fields: List[str] = ['Obscurity', 'Count', 'KGV1', 'Similarity1',
                                         'KGV2', 'Similarity2', 'KGV3', 'Similarity3']
                    csv_writer_a.writerow(fields)
                    csv_writer_b.writerow(fields)
    return lst_experiments


experiment_sim(obscure(existence()))

