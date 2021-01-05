import csv

alt_options = ['rewrite', 'skip']
rows = []
values_only = []
new_csv = []

with open (f'jaro_sim.csv', 'r') as file:
    csv_reader = csv.reader(file)
    fields = next(csv_reader)
#extracts first row of csvfile being the fields
    for row in csv_reader:
        rows.append(row)
#extracting each data row one by one
    for row in rows:
        for value in row:
            try:
                float(value)
            except ValueError:
                values_only.append(value)
#Removal of numeric values from rows
    values_only = [[values_only[value], values_only[value + 1], values_only[value + 2], values_only[value + 3]]
                   for value in range(0, len(values_only), 4)]
#Conversion of list back into tuples
    print(values_only)
    print(rows)
    print("Welcome to BMRB's data organization")
    start = input("To begin data organization type start: ")
    if start == 'start':
        for value in values_only:
            print(f'The acceptable options for {value[0]} are:')
            for number, string in enumerate((value[1:] + alt_options), start=1):
                print(f"{number, string}")
            choice = input("Your chosen option is?: ")
            if choice == '1':
                new_csv.append(value[1])
                print(new_csv)
            elif choice == '2':
                new_csv.append(value[2])
                print(new_csv)
            elif choice == '3':
                new_csv.append(value[3])
                print(new_csv)
            elif choice == '4':
                rewrite = input("What would you like to name this experiment?: ")
                new_csv.append(rewrite)
                print(new_csv)
            elif choice == '5':
                pass
    #user input to choose 1-5
    #if 1-3 are selected, add to new/updated csv file, print off next row to be analyzed
    #if 4 selected, user input then add to the updated csv file, print off next row to be analyzed
    #if skipped, send row to the end of the column, print off next row to be analyzed
    #if end of csv/column reached, end
    #if user input 'end', end



