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
            name, mark = line.split(",")
            students.append((name, int(mark)))
        except ValueError:
            print(f"Invalid record: {line}")

    return students

# Task3 - Grade calculator
def calculate_grade(marks):
