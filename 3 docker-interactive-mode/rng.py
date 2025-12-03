import random

min_number = int(input("Enter the minimum number: "))
max_number = int(input("Enter the maximum number: "))

if max_number<min_number:
    print('Invalid input - shutting down....')
else:
    rand_number = random.randint(min_number, max_number)
    print(f'Random number between {min_number} and {max_number} is {rand_number}')