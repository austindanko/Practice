import csv
import os
from typing import List, Union


def get_choice(values_only: [str]) -> [str]:
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
            with open('new_kdg.csv', 'a') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([values_only[0]])
            return values_only[0]
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


with open('jaro_sim.csv', 'r') as file_a, open('temp_file.csv', 'w') as file_b:
    csv_reader = csv.reader(file_a)
    csv_writer = csv.writer(file_b)
    csv_writer.writerow(next(csv_reader))
    try:
        for row in csv_reader:
            if len(row) >= 9:
                csv_writer.writerow(row)
            elif len(row) == 8:
                get_values(row)
                csv_writer.writerow(row)
            else:
                raise ValueError(f"Input file has row with wrong number of elements: {row}")
    except (KeyboardInterrupt, ValueError, SystemExit):
        csv_writer.writerow(row)
        for row in csv_reader:
            csv_writer.writerow(row)
    finally:
        os.rename('temp_file.csv', 'jaro_sim.csv')


