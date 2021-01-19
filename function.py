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