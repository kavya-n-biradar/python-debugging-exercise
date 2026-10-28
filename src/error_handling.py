"""Error handling with try-except: safe division and a marks file reader.

Run from the project root:
    python src/error_handling.py
"""

import logging
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKS_FILE = ROOT / "data" / "marks.txt"
LOG_FILE = ROOT / "logs" / "errors.log"


class InvalidMarkError(Exception):
    """Raised when a mark is outside the range 0 to 100."""


def setup_logging():
    """Send error messages to logs/errors.log."""
    LOG_FILE.parent.mkdir(exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.WARNING,
        format="%(asctime)s %(levelname)s %(message)s",
    )


def safe_divide(first, second):
    """Divide two numbers, handling bad input without crashing.

    Args:
        first: The number to divide.
        second: The number to divide by.

    Returns:
        float or None: The result, or None if the division is not possible.
    """
    try:
        result = first / second
    except ZeroDivisionError:
        print(f"  Cannot divide {first} by zero.")
        logging.warning("Division by zero: %s / %s", first, second)
        return None
    except TypeError:
        print(f"  Cannot divide {first!r} by {second!r}: not both numbers.")
        logging.warning("Type error: %r / %r", first, second)
        return None
    else:
        return result
    finally:
        print(f"  (attempted {first!r} / {second!r})")


def parse_mark(text):
    """Convert text to a mark between 0 and 100.

    Args:
        text (str): The mark as text.

    Returns:
        float: The mark as a number.

    Raises:
        ValueError: If the text is not a number.
        InvalidMarkError: If the number is below 0 or above 100.
    """
    mark = float(text)
    if not 0 <= mark <= 100:
        raise InvalidMarkError(f"mark {mark:g} is outside 0-100")
    return mark


def read_marks(path):
    """Read 'name,mark' lines, skipping and logging any bad lines.

    Args:
        path (Path or str): The file to read.

    Returns:
        dict: Valid marks as {name: mark}.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    marks = {}
    with open(path, "r", encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            try:
                name, text = line.strip().split(",")
                if not name.strip():
                    raise ValueError("name is empty")
                marks[name.strip()] = parse_mark(text)
            except InvalidMarkError as error:
                print(f"  Line {number}: {error}")
                logging.warning("Line %d: %s", number, error)
            except ValueError as error:
                print(f"  Line {number}: bad format ({error})")
                logging.warning("Line %d: bad format (%s)", number, error)
    return marks


def main():
    """Run the error handling demonstrations."""
    setup_logging()

    print("1. Safe division")
    for first, second in [(10, 2), (10, 0), (10, "x")]:
        print("  Result:", safe_divide(first, second))

    print("\n2. Reading a marks file with bad lines")
    try:
        marks = read_marks(MARKS_FILE)
    except FileNotFoundError:
        print(f"  The file {MARKS_FILE} was not found.")
        logging.error("Marks file missing: %s", MARKS_FILE)
        return
    else:
        print(f"  Loaded {len(marks)} valid marks: {marks}")
        if marks:
            print(f"  Class average: {sum(marks.values()) / len(marks):.1f}")

    print("\n3. A missing file")
    try:
        read_marks(ROOT / "data" / "missing.txt")
    except FileNotFoundError:
        print("  data/missing.txt does not exist, so nothing was read.")

    print(f"\nErrors were logged to {LOG_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()