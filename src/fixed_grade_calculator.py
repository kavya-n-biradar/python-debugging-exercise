"""Grade calculator (FIXED VERSION).

All bugs from buggy_grade_calculator.py have been identified and resolved.
See docs/debugging_report.md for the full list.
"""

students = {
    "Asha": [85, 90, 95],
    "Ravi": [55, 62, "48"],
    "Meera": [],
    "Kiran": [91, 88, 95],
}


def calculate_average(marks):
    """Return the average of a list of marks, or None if there are none.

    Marks given as text, such as "48", are converted to numbers. Marks
    that cannot be converted are skipped with a warning.

    Args:
        marks (list): The marks (numbers or numeric strings).

    Returns:
        float or None: The average, or None if there are no valid marks.
    """
    total = 0
    count = 0
    for mark in marks:  # Fix: loop over the items instead of using indexes
        try:
            total += int(mark)  # Fix: convert text such as "48" to a number
            count += 1
        except (ValueError, TypeError):
            print(f"  Warning: skipped invalid mark {mark!r}")
    if count == 0:  # Fix: avoid dividing by zero for an empty list
        return None
    return total / count


def get_grade(average):
    """Return a letter grade for an average mark."""
    if average >= 90:  # Fix: 90 itself should earn an A
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:  # Fix: added the missing colon
        return "F"


def main():
    """Print the average and grade of every student."""
    for name, marks in students.items():
        average = calculate_average(marks)
        if average is None:
            print(f"{name}: no marks recorded")
            continue
        grade = get_grade(average)  # Fix: corrected the typo "avrage"
        print(f"{name}: average {average:.1f}, grade {grade}")


if __name__ == "__main__":
    main()