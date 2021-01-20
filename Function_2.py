import csv
from typing import List, Union


# First, look at row, and determine if it already has a choice
# where to place...
# if len(row) > 8:
#    return row

def get_choice(values_only: [str]) -> Union[str, None]:
    alt_options = ['new_KGV', 'rewrite', 'skip', 'end']

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
        return values_only[0]
    elif choice == '5':
        rewrite = input("What would you like to name this experiment?: ")
        return rewrite
    elif choice == '6':
        return None
    elif choice == '7':
        quit()
    else:
        # TODO: Force them to choose again
        pass


def get_values(line) -> None:
    values_only = []
    for value in line:
        try:
            float(value)
        except ValueError:
            values_only.append(value)

    line.append(get_choice(values_only))
    csv_writer.writerow(line)


with open('jaro_sim.csv', 'r') as file_a, open('temp_file.csv', 'w') as file_b:
    csv_reader = csv.reader(file_a)
    csv_writer = csv.writer(file_b)
    next(csv_reader)
    for row in csv_reader:
        if len(row) >= 9:
            csv_writer.writerow(row)
        elif not row:
            print("CONGRATULATIONS")
            quit()
        elif len(row) == 8:
            get_values(row)
        else:
            raise ValueError(f"Input file has row with wrong number of elements: {row}")

# Rename a file
# os.rename('original_name', 'new_name')

# print("Welcome to BMRB's data organization")
# start = input("To begin data organization type start: ")
# if start == 'start':
#     row_num = input("Would you like to view the amount of faulty experiments? [Y/N]: ")
#     if row_num.upper() == 'Y':
#         print("Total no. of rows: %d" % (csv_reader.line_num))
#     else:
#         pass
