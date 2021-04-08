import operator
import os
from typing import Set, Dict, Iterable, List, Tuple, Union, Generator, Any
import csv
import requests
import pynmrstar
from strsimpy.jaro_winkler import JaroWinkler

def get_choice(values_only: List[str]) -> [str]:
    alt_options = ['new_KGV', 'rewrite', 'skip', 'end']
    count = 0

    while count < 3:
        count = count + 1
        print(f'The acceptable options for {values_only[0]} are:')
        for number, string in enumerate((values_only[1:] + alt_options), start=1):
            print(f"{number, string}")
        choice = input("Your chosen option is?: ")
        if choice == '1':
            return values_only[1]
        elif choice == '2':
            return values_only[2]
        elif choice == '3':
            return values_only[3]
        elif choice == '4':
            confirm = input('Would you like to use this as a new known good value "y" or "n" ')
            if confirm.lower() == 'y':
                with open('new_kgv.csv', 'a') as file_new_kgv:
                    csv_writer = csv.writer(file_new_kgv)
                    csv_writer.writerow([values_only[0]])
                return values_only[0]
            else:
                rewrite = input("What would you like to name this experiment?: ")
                with open('new_kgv.csv', 'a') as file_new_kgv:
                    csv_writer = csv.writer(file_new_kgv)
                    csv_writer.writerow([rewrite])
                return rewrite
        elif choice == '5':
            rewrite = input("What would you like to name this experiment?: ")
            return rewrite
        elif choice == '6':
            return None
        elif choice == '7':
            raise SystemExit('User Quit')
        else:
            print('Chose option between 1-7')

    raise ValueError('UNACCEPTABLE OPTION')


def get_values(original_row: [Union[str, float]]) -> None:
    values_only = []
    for value in original_row:
        try:
            float(value)
        except ValueError:
            values_only.append(value)

    user_choice = get_choice(values_only)
    original_row.append(user_choice)


def obscure(experiments: List[str]) -> List[str]:
    obscurities: List[str] = []
    current_known_good_values = get_known_good_values()
    for obscurity in experiments:
        if obscurity not in current_known_good_values and obscurity not in pynmrstar.definitions.NULL_VALUES:
            obscurities.append(obscurity)
    return obscurities


def create_or_update_matches(obscurities: List[str]) -> None:
    if not os.path.exists('jaro_sim.csv'):
        print('Running experiment similarities...')
        jaro = JaroWinkler().similarity
        obscurity_count: Dict[str, bool] = {x: obscurities.count(x) for x in obscurities}
        with open('jaro_sim.csv', 'a') as file_jaro_sim, \
                open('jaro_sim_orphan.csv', 'a') as file_jaro_sim_orphan:
            jaro_csv_writer = csv.writer(file_jaro_sim)
            orphan_csv_writer = csv.writer(file_jaro_sim_orphan)
            fields: List[str] = ['Obscurity', 'Count', 'KGV1', 'Similarity1',
                                 'KGV2', 'Similarity2', 'KGV3', 'Similarity3']
            jaro_csv_writer.writerow(fields)
            orphan_csv_writer.writerow(fields)

            current_known_good_values = get_known_good_values()
            for obscurity in set(sorted(obscurities)):
                sim_val: List[Tuple[str, float]] = []
                for good_value in current_known_good_values:
                    similarity_value: float = jaro(obscurity, good_value)
                    sim_val.append((good_value, similarity_value))
                    sim_val.sort(reverse=True, key=operator.itemgetter(1))
                topthree: List[Union[str, float, int]] = []
                topthree.extend([x for y in sim_val[:3] for x in y])
                output = [obscurity, obscurity_count[obscurity]] + topthree
                if obscurity_count[obscurity] <= 10:
                    orphan_csv_writer.writerow(output)
                else:
                    jaro_csv_writer.writerow(output)
    else:
        print('Simulation file already exists.')
        return


def get_and_cache_experiments() -> List[str]:
    api_sourced_experiments: List[str] = []

    if not os.path.exists('api.bmrb.csv'):
        print("Regenerating experiments from API...")
        all_entries: Iterable[pynmrstar.Entry] = pynmrstar.utils.iter_entries()
        print('Running api.bmrb...')
        for entry in all_entries:
            value = entry.get_tag('_Experiment.Name')
            api_sourced_experiments.extend(value)
        with open('api.bmrb.csv', 'w') as file_api:
            api_csv_writer = csv.writer(file_api)
            api_csv_writer.writerow(api_sourced_experiments)
        return api_sourced_experiments
    else:
        print('Reading experiments from local cache...')
        with open('api.bmrb.csv', 'r') as file_api:
            api_csv_reader = csv.reader(file_api)
            return next(api_csv_reader)


def get_known_good_values() -> Set[str]:
    print('Loading known good values from API and local file...')
    api_good_values: Set[str] = set(
        requests.get('https://api.bmrb.io/v2/enumerations/_Experiment.Name').json()['values'])

    if os.path.exists('new_kgv.csv'):
        with open('new_kgv.csv', 'r') as file_new_kgv:
            csv_reader = csv.reader(file_new_kgv)
            local_good_values = set([_ for _ in csv_reader])
            all_good_values = api_good_values | local_good_values
            return all_good_values
    else:
        return api_good_values


def user_input():
    with open('jaro_sim.csv', 'r') as file_jaro_sim, open('temp_file.csv', 'w') as file_temp:
        jaro_csv_reader = csv.reader(file_jaro_sim)
        temp_csv_writer = csv.writer(file_temp)
        temp_csv_writer.writerow(next(jaro_csv_reader))
        try:
            for row in jaro_csv_reader:
                if len(row) >= 9:
                    temp_csv_writer.writerow(row)
                elif len(row) == 8:
                    get_values(row)
                    temp_csv_writer.writerow(row)
                else:
                    raise ValueError(f"Input file has row with wrong number of elements: {row}")
        except (KeyboardInterrupt, ValueError, SystemExit):
            temp_csv_writer.writerow(row)
            for row in jaro_csv_reader:
                temp_csv_writer.writerow(row)
        finally:
            os.rename('temp_file.csv', 'jaro_sim.csv')


experiments = get_and_cache_experiments()
obscurities = obscure(experiments)
create_or_update_matches(obscurities)
user_input()

