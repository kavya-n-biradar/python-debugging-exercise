# Error Handling and Debugging in Python

A Python project for the CodeMore Python Programming Internship (Week 4, Task 3). It demonstrates error handling with `try-except` blocks and shows how a buggy script was debugged step by step.

## Project Overview

- `src/error_handling.py` demonstrates `try / except / else / finally`, a custom exception, reading a file with bad lines, and logging errors.
- `src/buggy_grade_calculator.py` is the original script with six deliberate bugs.
- `src/fixed_grade_calculator.py` is the debugged version.
- `docs/debugging_report.md` documents every bug: the error, the cause, how it was found and how it was fixed, plus a `pdb` session.

## Project Structure

```
python-debugging-exercise/
├── README.md
├── .gitignore
├── src/
│   ├── error_handling.py
│   ├── buggy_grade_calculator.py
│   └── fixed_grade_calculator.py
├── data/
│   └── marks.txt
└── docs/
    ├── debugging_report.md
    └── screenshots/
```

## Requirements

- Python 3.8 or newer. No external libraries.

## Setup and How to Run

```bash
git clone https://github.com/kavya-n-biradar/python-debugging-exercise.git
cd python-debugging-exercise
python src/error_handling.py
python src/fixed_grade_calculator.py
```

`src/buggy_grade_calculator.py` is kept only to show the "before" state. It will not run, because it starts with a syntax error.

## Bugs Found and Fixed

| # | Type | Error | Fix |
|---|---|---|---|
| 1 | Syntax error | `SyntaxError: expected ':'` | Added the missing colon after `else` |
| 2 | Runtime error | `IndexError` | Looped over items instead of `range(len(marks) + 1)` |
| 3 | Runtime error | `NameError` | Fixed the typo `avrage` |
| 4 | Runtime error | `TypeError` | Converted text marks with `int()` |
| 5 | Runtime error | `ZeroDivisionError` | Handled an empty list |
| 6 | Logic error | Wrong grade at 90 | Changed `>` to `>=` |

## Error Handling Concepts Used

- `try / except` with specific exception types
- `else` (runs when no error happens) and `finally` (always runs)
- Custom exception (`InvalidMarkError`) and `raise`
- Reading a file safely, handling `FileNotFoundError` and bad lines
- The `logging` module to record errors in `logs/errors.log`
- `pdb` for stepping through code and inspecting variables

## Console Output

### Fixed grade calculator
```
Asha: average 90.0, grade A
Ravi: average 55.0, grade C
Meera: no marks recorded
Kiran: average 91.3, grade A
```

### `error_handling.py` (shortened)
```
  Cannot divide 10 by zero.
  Line 3: bad format (could not convert string to float: 'abc')
  Line 5: mark 105 is outside 0-100
  Loaded 4 valid marks: {'Asha': 85.0, 'Ravi': 72.0, 'Isha': 91.0, 'Neha': 67.5}
  Class average: 78.9
```

## Screenshots

Full screenshots are in [`docs/screenshots/`](docs/screenshots/):
- `bug1_syntax_error.png` to `bug6_logic_error.png`: the error at each debugging step
- `pdb_session1.png` and `pdb_session2.png`: using the `pdb` debugger
- `fixed_output.png`: the corrected program output
- `error_handling_output.png` and `error_log_file.png`: the error handling program and its log

## What I Learned

- How to read a traceback from the bottom to find the cause
- The difference between syntax errors, runtime errors and logic errors
- How to debug by fixing one bug at a time
- How to use `try / except / else / finally`, custom exceptions and logging
- How to use `pdb` to inspect variables while a program runs

## Author

Kavya Biradar