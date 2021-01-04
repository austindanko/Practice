import csv

alt_options = ['rewrite', 'skip']
rows = []
new_csv = []

with open (f'jaro_sim.csv', 'r') as file:
    csv_reader = csv.reader(file)
    fields = next(csv_reader)
#extracts first row of csvfile being the fields
    for row in csv_reader:
        rows.append(row)
#extracting each data row one by one

    print("Welcome to BMRB's data organization")
    start = input("To begin data organization type start: ")
    if start == 'start':
        print(f'The acceptable options for {rows[0][0]} are:')
        for number, string in enumerate((rows[0][1:] + alt_options), start=1):
            print(f"{number, string}")
        choice = input("Your chosen option is?: ")
        if choice == '1':
            new_csv.append(rows[1])
            print(new_csv)
        elif choice == '2':
            new_csv.append(rows[2])
            print(new_csv)
        elif choice == '3':
            new_csv.append(rows[3])
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



