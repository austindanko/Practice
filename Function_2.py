


letters = ('a', 'b', 'c', 'd', 'e')

print("Welcome to BMRB's data organization")
start = input("To begin data organization type start: ")
if start == 'start':
    print(f'The acceptable options for {letters[:1]} are:')
    for number, letter in enumerate(letters[1:]):
        print(f"{number, letter}")


