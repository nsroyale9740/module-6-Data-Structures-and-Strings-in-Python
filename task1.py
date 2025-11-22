student = {}
n = int(input("How many students do you want to add? "))

for i in range(n):
    name = input("Enter student name: ").strip().title()
    marks = int(input("Enter marks: "))
    student[name] = marks

print("Student Dictionary:", student)

def get_student_marks(name):
    if name in student:
        print(f"{name}'s marks: {student[name]}")
    else:
        print("Student not found.")

get_student_marks(input("Enter student name to retrieve marks: ").strip().title())




# students = {"John": 85,"Alice": 90,"Bob": 78}

# user_input = input("Enter student name: ").strip().title() 

# if user_input in students:
#     print(f"{user_input}'s marks: {students[user_input]}")
# else:
#     print("Student not found.") 
