import csv
from typing import List, Union

# First, look at row, and determine if it already has a choice
# where to place...
#if len(row) > 8:
#    return row

def get_choice(values_only):

    alt_options = ['new_KGV', 'rewrite', 'skip', 'end']

    print(f'The acceptable options for {values_only[0]} are:')
    for number, string in enumerate((values_only[1:] + alt_options), start=1):
        print(f"{number, string}")
    choice = input("Your chosen option is?: ")
    if choice == '1':
        #value one
        pass
    elif choice == '2':
        #value two
        pass
    elif choice == '3':
        #value 3
        pass
    elif choice == '4':
        #new_KGV
        pass
    elif choice == '5':
        #rewrite
        rewrite = input("What would you like to name this experiment?: ")
        pass
    elif choice == '6':
        #skip
        pass
    elif choice == '7':
        #end
        quit()


def get_values(row) -> List[str]:
    values_only = []
    for value in row:
        try:
            float(value)
        except ValueError:
            values_only.append(value)
    get_choice(values_only)


with open(f'jaro_sim.csv', 'r') as file_a, open(f'temp_file.csv', 'w') as file_b:
    csv_reader = csv.reader(file_a)
    csv_writer = csv.writer(file_b)
    next(csv_reader, None)
    for row in csv_reader:
        get_values(row)



# Rename a file
#os.rename('original_name', 'new_name')

# print("Welcome to BMRB's data organization")
# start = input("To begin data organization type start: ")
# if start == 'start':
#     row_num = input("Would you like to view the amount of faulty experiments? [Y/N]: ")
#     if row_num.upper() == 'Y':
#         print("Total no. of rows: %d" % (csv_reader.line_num))
#     else:
#         pass



