import csv

alt_options = ['rewrite', 'skip', 'end']
rows = []
values_only = []
user_input = []

with open (f'jaro_sim.csv', 'r') as file:
    csv_reader = csv.reader(file)
    fields = next(csv_reader)
#extracts first row of csvfile being the fields
    for row in csv_reader:
        rows.append(row)
#extracting each data row one by one
        for value in row:
            try:
                float(value)
            except ValueError:
                values_only.append(value)
#Removal of numeric values from rows
    values_only = [[values_only[value], values_only[value + 1], values_only[value + 2], values_only[value + 3]]
                   for value in range(0, len(values_only), 400)]
#Conversion of list back into tuples

    print("Welcome to BMRB's data organization")
    start = input("To begin data organization type start: ")
    if start == 'start':
        row_num = input("Would you like to view the amount of faulty experiments? [Y/N]: ")
        if row_num.upper() == 'Y':
            print("Total no. of rows: %d" % (csv_reader.line_num))
        else:
            pass
        for value in values_only:
            print(f'The acceptable options for {value[0]} are:')
            for number, string in enumerate((value[1:] + alt_options), start=1):
                print(f"{number, string}")
            choice = input("Your chosen option is?: ")
            if choice == '1':
                user_input.append(value[1])
            elif choice == '2':
                user_input.append(value[2])
            elif choice == '3':
                user_input.append(value[3])
            elif choice == '4':
                rewrite = input("What would you like to name this experiment?: ")
                user_input.append(rewrite)
            elif choice == '5':
                pass
            elif choice == '6':
                quit()


