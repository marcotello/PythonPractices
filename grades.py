names =  input("Enter the names separated by commas: ") # get and process input for a list of names
assignments =  input("Enter the assignments separated by commas: ")
grades =  input("Enter the grades separated by commas: ") # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

names_list = names.split(',')
assignments_list = assignments.split(',')
grades_list = grades.split(',')

items_list = zip(names_list, assignments_list, grades_list)

def sum_missing_assignment(assigment, grade):
    return int(grade) + int(assigment) * 2

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assigment, grade in items_list:
    print("Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n".format(name, grade, assigment, sum_missing_assignment(assigment, grade)))