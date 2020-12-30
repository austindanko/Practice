
alt_options = ('rewrite', 'skip')
csvfile = ('obscurity', 'KGV1', 'KGV2', 'KGV3') + alt_options
#for actual csv file have code skip over integers, to create a list similar to above^






print("Welcome to BMRB's data organization")
start = input("To begin data organization type start: ")
if start == 'start':
    print(f'The acceptable options for {csvfile[:1]} are:')
    for number, letter in enumerate(csvfile[1:]):
        print(f"{number, letter}")
    #user input to choose 0-4
    #if 0-2 are selected, add to new/updated csv file, print off next row to be analyzed
    #if 3 selected, user input then add to the updated csv file, print off next row to be analyzed
    #if skipped, send row to the end of the column, print off next row to be analyzed
    #if end of csv/column reached, end
    #if user input 'end', end



