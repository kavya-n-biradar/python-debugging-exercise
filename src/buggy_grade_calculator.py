"""Grade calculator (BUGGY VERSION).

This script contains several deliberate bugs that were found and fixed.
See docs/debugging_report.md and src/fixed_grade_calculator.py.
"""

students = {
    "Asha": [85, 90, 95],
    "Ravi": [55, 62, "48"],
    "Meera": [],
    "Kiran": [91, 88, 95],
}


def calculate_average(marks):
    """Return the average of a list of marks."""
    total = 0
    for i in range(len(marks) + 1):
        total += marks[i]
    return total / len(marks)


def get_grade(average):
    """Return a letter grade for an average mark."""
    if average > 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else
        return "F"


def main():
    """Print the average and grade of every student."""
    for name, marks in students.items():
        average = calculate_average(marks)
        grade = get_grade(avrage)
        print(f"{name}: average {average:.1f}, grade {grade}")


if __name__ == "__main__":
    main()