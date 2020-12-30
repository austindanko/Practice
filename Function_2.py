
alt_options = ('rewrite', 'skip')
csvfile = ('obscurity', 'KGV1', 'KGV2', 'KGV3') + alt_options
#for actual csv file have code skip over integers, to create a list similar to above^


new_csv = []



print("Welcome to BMRB's data organization")
start = input("To begin data organization type start: ")
if start == 'start':
    print(f'The acceptable options for {csvfile[:1]} are:')
    for number, string in enumerate(csvfile[1:], start=1):
        print(f"{number, string}")
    choice = input("Your chosen option is?: ")
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    #user input to choose 1-5
    #if 1-3 are selected, add to new/updated csv file, print off next row to be analyzed
    #if 4 selected, user input then add to the updated csv file, print off next row to be analyzed
    #if skipped, send row to the end of the column, print off next row to be analyzed
    #if end of csv/column reached, end
    #if user input 'end', end



