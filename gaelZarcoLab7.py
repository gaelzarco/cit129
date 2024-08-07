###
# Name: Gael Zarco
# Course and Section: CIT 129 - 1002 - 1003
# Purpose: Manage and display students' test scores, including validation, sorting, and individual score lookup.
###

# Returns seconds element in a tuple
def get_second_element(tup):
    return tup[1]

# Used this instead of zip to practice 
# Merges two arrays as an array of tuples, sorted in ascending order
def arr_merge_sort(arr, arr2):
    # The value used to iterate through the array is determined by smallest array length
    itr = min([len(arr), len(arr2)])
    # Initialize empty array to append tuple values to during array traversal
    tup_arr = []
    # Traversing both arrays, ensuring to push values that exist at the same index in BOTH arrays
    for i in range(itr):
        if arr[i] and arr2[i]:
            # Appending these values as a tuple
            tup_arr.append((arr[i], arr2[i]))

    # Sorting the array of tuples in default ascending order using the value at index 1 of each tuple as the key
    sorted_tup_arr = sorted(tup_arr, key=get_second_element)
    # Return final tuple arr
    return sorted_tup_arr

students = int(input('Enter amount of students in class: '))

while students > 10 or students < 1:
    students = int(input('Please enter a value between 1 and 10: '))

students_names = []
students_scores = []

for student in range(students):
    student_score = int(input(f"Please enter student {student + 1}'s score: "))
    student_name = input(f"Please enter student {student + 1}'s name: ")
    students_scores.append(student_score)
    students_names.append(student_name)

print('\n*** GRADE REPORT')
for student in range(students):
    print(f"{students_names[student]}: {students_scores[student]}")

# Print highest score
print(f"The highest score: {max(students_scores)}")

# Use of custom arr_merge_sort function
sorted_students = arr_merge_sort(students_names, students_scores)

# Index intro array of tuples and index into first element and second element of tuple respectively to get name: score
print('\n*** FINAL Grade Report – Sorted by scores ***')
for student in range(students):
    print(f"{sorted_students[student][0]}: {sorted_students[student][1]}")

# Boolean variable to set conditional loop
found_student_bool = False

# Conditional loop where chosen_student is checked to see if it is a valid student name in the array of students_names
while not found_student_bool:
    chosen_student = input("Please enter a student's name to fetch their score: ")

    # Check to see if student's name exists and prints score
    for student in range(students):
        if students_names[student] == chosen_student:
            score = students_scores[student]
            # Updates loop condition if found
            found_student_bool = True
            print(f"{chosen_student}'s score is: {score}")
