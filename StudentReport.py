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

        elif mark > 79 and mark < 90:
            grade = "B"

        elif mark > 59 and mark < 80:
            grade = "C"

        else:
            grade = "D"

        graded.append((name, mark, grade))
    return graded


# Task4 - Write Output File
def write_results(file_path_output, graded):
    from pathlib import Path
    from datetime import datetime
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"Students Graded {timestamp}.txt"
        full_path = Path(file_path_output) / filename
        with open(full_path, "w") as f:
            for name, mark, grade in graded:
                f.write(f"{name}, {mark}, {grade}\n")
        return True
    except Exception as e:
        return False


# Task5 - Report Generator
def generate_report(file_path, file_path_output, graded):
    total_students = len(graded)
    sum_marks = 0
    counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for _, mark, grade in graded:
        sum_marks += mark
        counts[grade] += 1

    average_mark = sum_marks / total_students if total_students else 0

    print(f"""
    Input file path: {file_path}
    Output file path: {file_path_output}
        *** Students grades report ***
        Total Students: {total_students}
        Average Mark: {average_mark}
        Number of A grades: {counts["A"]}
        Number of B grades: {counts["B"]}
        Number of C grades: {counts["C"]}
        Number of D grades: {counts["D"]}""")


def main():
    file_path = input("Enter absolute file path: ")
    file_path_output = input("Enter absolute output file path: ")
    lines = read_students(file_path)
    students = process_students(lines)
    graded = calculate_grade(students)
    write_results_bool = write_results(file_path_output, graded)
    if write_results_bool:
        generate_report(file_path, file_path_output, graded)
        print("The output file is written successfully.")
    else:
        print("Something went wrong.")


if __name__ == "__main__":
    main()
