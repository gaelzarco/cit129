###
# Name: Gael Zarco
# Course and Section: CIT 129 - 1002 - 1003
# Date of Completion: 07/18/24
# Time To Complete: 25 Minutes
# Purpose: Password protected, average temperature calculator for any amount of rooms readings.
###

password = input('Enter the password: ')
while int(password) != 123:
    password = input('Incorrect password. Please try again: ')

rooms = int(input('Please enter the number of rooms: '))
collective_temp = 0
collective_readings = 0

for room in range(rooms):
    temp_readings = int(input('Please enter the amount of times to conduct a temperature reading: '))
    collective_readings += temp_readings
    total_temp = 0
    for t in range(temp_readings):
        temp = int(input('Enter temperature: '))
        total_temp += temp
    average_temp = total_temp / temp_readings
    collective_temp += total_temp
    print(f"Total temperature for one room: {total_temp:.2f}")
    print(f"Average temperature for one room: {average_temp:.2f}\n")

collective_average = collective_temp / collective_readings
print('FINAL TEMPERATURE REPORT')
print(f"\nTotal temperature for all rooms: {collective_temp:.2f}")
print(f"Average temperature for all rooms: {collective_average:.2f}")
