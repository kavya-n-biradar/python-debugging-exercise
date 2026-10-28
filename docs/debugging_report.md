# Debugging Report

## Overview

`src/buggy_grade_calculator.py` is a grade calculator that contained six bugs of three kinds: a syntax error, runtime errors and a logic error. This report shows how each bug was found, why it happened and how it was fixed. The corrected program is `src/fixed_grade_calculator.py`.

## Debugging process

1. **Run the program** and read the error message.
2. **Read the traceback from the bottom.** The last line names the error, and the lines above show where it happened.
3. **Find the cause** by inspecting the values involved, using `print()` or the `pdb` debugger.
4. **Fix one bug at a time,** and run again to check the fix and reveal the next bug.
5. **Check the output is correct,** not just that the program runs.

## Summary of bugs

| # | Type | Error | Location | Fix |
|---|---|---|---|---|
| 1 | Syntax error | `SyntaxError: expected ':'` | `get_grade`, the `else` line | Added the missing colon |
| 2 | Runtime error | `IndexError: list index out of range` | `calculate_average`, `range(len(marks) + 1)` | Looped over the marks directly |
| 3 | Runtime error | `NameError: name 'avrage' is not defined` | `main`, `get_grade(avrage)` | Fixed the typo |
| 4 | Runtime error | `TypeError: unsupported operand type(s) for +=: 'int' and 'str'` |