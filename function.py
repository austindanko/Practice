#!/usr/bin/python3

def get_choice(iteration=0) -> bool:

    if iteration == 2:
        print("Why was that so hard?")
        raise ValueError('User refused to choose.')
    choice = input("y or n?")
    if choice == 'y':
        return True
    elif choice == 'n':
        return False
    else:
        print('Invalid choice. Please choose from "y" or "n".')
        return get_choice(iteration+1)

get_choice()

# New behavior:

# One program that does all of the following

*) For choice 4, allow the user to specify a new known good value rather then just using what was there
*) First checks if jaro_csv exists, if not create it (using the new known good value)
*) Once it exists, then start prompting the user for their choices
*) If the user specifies a new known good value, recalulculate all lines in the CSV in which they have not made a choice
*) User continues