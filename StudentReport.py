

# Task1 - File reader
def read_students(file_path):
    lines = []

    try:
        with open(file_path, "r") as file:
            content = file.read()

            if not content:
                print("File is empty.")
                return []

            lines = content.splitlines()
            return lines

    except FileNotFoundError:
        print("File not found.")
        return []


# Task2 - Data Processing with List/Tuples
def process_students(lines):
    students = []

    for line in lines:
        try:
            student_id, name, mark = line.split(",")
            students.append((student_id, name, int(mark)))
        except ValueError:
            print(f"Invalid record: {line}")

    return students

# Task3 - Grade calculator
def calculate_grade(students):
    graded = []
    for student_id, name, mark in students:

        if mark > 89:
            grade = "A"

        elif mark > 79  and mark < 90:
            grade = "B"

        elif mark > 59 and mark < 80:
            grade = "C"

        else: grade = "D"

        graded.append((student_id, name, mark, grade))
    return graded

# Task4 - Write Output File
def write_results(file_path_output, graded):
    from pathlib import Path
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename =f"Students Graded {timestamp}.txt"
    full_path = Path(file_path_output) / filename
    with open(f"{full_path}", "w") as f:
        for student_id, name, mark, grade in graded:
            f.write(f"{student_id}, {name}, {mark}, {grade}\n")

# Task5 - Report Generator
def generate_report(graded):
    file_path = input("Enter file path")
    file_path_output = input("Enter path to save new file")

    total_students = len(graded)
    average_marks = 0
    numbers_of_A = 0
    numbers_of_B = 0
    numbers_of_C = 0
    numbers_of_D = 0

    for student_id in graded:
        average_marks += average_marks
