student_marks = {
    "Heama": 85,
    "Kavya": 92,
    "keerhty": 88,
    "divya": 90,
    "gomathi": 88,
    "deepthi":94
}

# Ask user to input a student name
name = input("Enter the student's name: ")

# Check if the name exists in the dictionary
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"No record found for student '{name}'.")
