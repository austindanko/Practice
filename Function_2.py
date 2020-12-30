
alt_options = ('rewrite', 'skip')
csvfile = ('obscurity', 'KGV1', 'KGV2', 'KGV3') + alt_options
#for actual csv file have code skip over integers, to create a list similar to above^


new_csv = []
#just a list for now, for an actuall csv file each choice would be writing a new row to said file



print("Welcome to BMRB's data organization")
start = input("To begin data organization type start: ")
if start == 'start':
    print(f'The acceptable options for {csvfile[:1]} are:')
    for number, string in enumerate(csvfile[1:], start=1):
        print(f"{number, string}")
    choice = input("Your chosen option is?: ")
    if choice == '1':
        new_csv.append(csvfile[1])
        print(new_csv)
    elif choice == '2':
        new_csv.append(csvfile[2])
        print(new_csv)
    elif choice == '3':
        new_csv.append(csvfile[3])
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



