"""
Grade Central - Student Management System

A command-line application for managing student records.

Features:
- Add grades to existing students
- Remove students
- View average grades

Notes:
- Data is stored in memory (not persistent)
- Authentication is basic and not secure
"""

from statistics import mean

# Demo admin credentials (plain-text, not secure)
admins = {"Python": "Pass123@"}

# Student records: {student_name: [grades]}
# Assumes student names are unique identifiers
student_dict = {
    "Jeff": [],
    "Alex": [],
    "Sam": []
}

def enter_grades():
    """
    Add a grade to an existing student.

    Flow:
    - Read student name and grade
    - Verify student exists
    - Append grade to student's record

    Limitations:
    - No input validation for non-numeric grades (may crash)
    - No range checks (e.g., negative or >100 allowed)
    """
    name_to_enter = input("Student Name: ")
    grade_to_enter = input("Grade: ")

    if name_to_enter in student_dict:
        print("Adding Grade...")
        student_dict[name_to_enter].append(float(grade_to_enter))  # May raise ValueError
    else:
        print("Student does not exist.")

    print(student_dict)


def remove_student():
    """
    Remove a student from the system.

    Warning:
    - Operation is irreversible (no backup or confirmation)
    """
    name_to_remove = input("What student to remove?: ")

    if name_to_remove in student_dict:
        print("Removing student...")
        del student_dict[name_to_remove]
        print(student_dict)
    else:
        print("Student does not exist.")


def student_avgs():
    """
    Display average grade for each student.

    Handles:
    - Skips empty grade lists to avoid mean([]) error
    """
    for student in student_dict:
        grade_list = student_dict[student]

        if len(grade_list) == 0:
            print(student, "has no grades yet.")
        else:
            avg_grade = mean(grade_list)
            print(student, "has an average of:", avg_grade)


def main():
    """
    Menu controller.

    Displays options and routes user input to corresponding actions.
    Runs repeatedly via external loop.
    """
    print("""
    Welcome to Grade Central

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)

    action = input("What would you like to do today? (Enter a number): ")

    if action == "1":
        enter_grades()
    elif action == "2":
        remove_student()
    elif action == "3":
        student_avgs()
    elif action == "4":
        print("Exiting...")
        exit()
    else:
        print("No valid input choice was given, try again")


# --- Authentication Section ---
# Basic login system using hardcoded credentials (for demo only)

login = input("Username: ")
passw = input("Password: ")

if login in admins:
    if admins[login] == passw:
        print("Welcome,", login)

        # Keeps application running until user exits manually
        while True:
            main()
    else:
        print("Invalid password!")
else:
    print("Invalid username!")