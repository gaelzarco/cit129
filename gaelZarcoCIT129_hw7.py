###
# Name: Gael Zarco
# Course and Section: CIT 129 - 1002 - 1003
# Date of Completion: 07/29/24
# Time To Complete: 80 Minutes
# Purpose: Calculate and print reports of worker pay with search functionality
###

employees = int(input("Please enter the amount of employees to calculate pay for: "))

# Verify that amount of employees is valid
while employees < 1 or employees > 150:
    employees = int(input("Please enter an amount between 1 and 50. Amount of employees: "))

# Initialize employee info arrays
employees_hours = []
employees_last_names = []
employees_pay_rates = []

# Prompt user for employee info
for i in range(employees):
    emp_hours = float(input(f"Please enter the amount of hours worked by employee {i + 1}: "))
    emp_last_name = input(f"Please enter the last name of employee {i + 1}: ")
    emp_pay_rate = float(input(f"Please enter the pay rate of employee {i + 1}: "))

    employees_hours.append(emp_hours)
    employees_last_names.append(emp_last_name)
    employees_pay_rates.append(emp_pay_rate)
    
# Begin first report print
print("\nEMPLOYEE REPORT 01/01/2024")
# Print formatted table headers
print("{:<10} {:<10} {:<9}".format("Name", "Hours Worked", "Pay Rate"))

# Print formatted tables rows, iterating and printing every value incrementally in all 3 arrays.
for i in range(employees):
    print("{:<10} {:<13.2f} ${:<9.2f}".format(employees_last_names[i], employees_hours[i], employees_pay_rates[i]))

# Create and populate array for all employee's total pay
employees_total_pay = []

# Begin calculting total pay for each individual employee, ensuring to double the total pay for workers who worked overtime
for i in range(employees):
    total_emp_pay = employees_hours[i] * employees_pay_rates[i]
    
    # Calculating and applying overime pay
    if employees_hours[i] > 40:
        total_emp_pay = total_emp_pay * 2

    employees_total_pay.append(total_emp_pay)

# Calculate total pay with sum()
total_pay = sum(employees_total_pay)
# Calculate average pay
average_pay = total_pay / employees
        
# Begin final report print
print("\nFINAL REPORT 01/01/2024")

# Print formatted table headers
print("{:<10} {:<10} {:<9} {:<8}".format("Name", "Hours Worked", "Pay Rate", "Total Pay"))

# Print formatted tables rows, iterating and printing every value incrementally in all 4 arrays.
for i in range(employees):
    print("{:<10} {:<13.2f} ${:<9.2f} ${:<8.2f}".format(employees_last_names[i], employees_hours[i], employees_pay_rates[i], employees_total_pay[i]))

# Print previously calculated averages and totals
print("\nTOTAL PAY for all employees = ${:.2f}".format(total_pay))
print("AVERAGE PAY for all employees = ${:.2f}".format(average_pay))

# Begin search feature and take intitial input
search_condition = input("\nPlease enter an employee's last name for details. (enter 'exit' when finished): ")

# Verify that user does not want to exit the program yet
while search_condition != "exit":
   # Iterate over employee last names and print all related information
   for i in range(employees):
       if employees_last_names[i] == search_condition:
           print("The total pay for {} is ${:.2f}. Their pay rate is ${:.2f} and they worked {}".format(employees_last_names[i], employees_total_pay[i], employees_pay_rates[i], employees_hours[i])) 
           # Allow user to search for another user or end program
           search_condition = input("\nPlease enter an employee's last name for details. (enter 'exit' when finished): ")
           
            
