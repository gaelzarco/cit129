###
# Name: Gael Zarco
# Course and Section: CIT 129 - 1002 - 1003
# Date of Completion: 07/21/24
# Time To Complete: 40 Minutes
# Purpose: Password protected, CLI, letter to num pad converter. This program takes in a string size and converts each character in the string to a number corresponding to that letter on a num pad.
###

# Check for password with automated validation
password = input('Enter the password: ')
while password != 'phone':
    password = input('Incorrect password. Please try again: ')

# Check for max amount of letters
max_chars = int(input('Enter the amount of letters you will enter (1-10): '))
while max_chars <= 0 or max_chars > 10:
    max_chars = int(input('Invalid amount of letters. Please enter something between 1 and 10: '))

# Final report variables
chars_entered = 0
valid_chars = 0
invalid_chars = 0

count = 0

# User input for each letter in specified string size 
while count < max_chars:
    # Input variable
    curr_char = input(f"\nInput letter {count + 1}: ")

    # Verifying validity and assigning input to a number on num pad
    # Incrementing stats for report generation
    if curr_char == 'A' or curr_char == 'B' or curr_char == 'C':
        valid_chars = valid_chars + 1
        print(2)
    elif curr_char == 'D' or curr_char == 'E' or curr_char == 'F':
        valid_chars = valid_chars + 1
        print(3)
    elif curr_char == 'G' or curr_char == 'H' or curr_char == 'I':
        valid_chars = valid_chars + 1
        print(4)
    elif curr_char == 'J' or curr_char == 'K' or curr_char == 'L':
        valid_chars = valid_chars + 1
        print(5)
    elif curr_char == 'M' or curr_char == 'N' or curr_char == 'O':
        valid_chars = valid_chars + 1
        print(6)
    elif curr_char == 'P' or curr_char == 'Q' or curr_char == 'R' or curr_char == 'S':
        valid_chars = valid_chars + 1
        print(7)
    elif curr_char == 'T' or curr_char == 'U' or curr_char == 'V':
        valid_chars = valid_chars + 1
        print(8)
    elif curr_char == 'W' or curr_char == 'X' or curr_char == 'Y' or curr_char == 'Z':
        valid_chars = valid_chars + 1
        print(9)
    # Action if character is not a capital letter
    else:
        invalid_chars = invalid_chars + 1
        print("Invalid input. Please enter only capital letters.")

    # Continues loop and increments report stats
    chars_entered = chars_entered + 1
    count = count + 1

# Print report
print(f"\nNumber of letters entered: {chars_entered}")
print(f"Number of valid letters entered: {valid_chars}")
print(f"Number of invalid letters entered: {invalid_chars}")
