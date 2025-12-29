#!/usr/bin/env python3

"""
Here I had to use some help since I'm not a pro
in Linear Programming (LP) and Integer Optimization.
I learnt it, but it was long forgotten.

Z3 is also new to me.
"""

import re

from z3 import Int, Optimize, Sum, sat

# from z3 import *

Button = tuple[int, ...]


def parse_line(line: str) -> tuple[list[Button], list[int]]:
    """
    Parses a line like:
    [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

    Returns: (buttons, targets)
    where buttons is list of tuples, targets is list of ints
    """
    # Find all button patterns (between parentheses)
    button_matches = re.findall(r"\(([^)]+)\)", line)

    buttons: list[Button] = []
    for btn_str in button_matches:
        # Skip if it's empty or looks like part of the light diagram
        if btn_str and not btn_str.startswith("["):
            # Convert comma-separated numbers to tuple of ints
            btn_tuple = tuple(map(int, btn_str.split(",")))
            buttons.append(btn_tuple)

    # Find joltage requirements (between curly braces)
    joltage_match = re.search(r"\{([^}]+)\}", line)
    if joltage_match:
        joltage_str = joltage_match.group(1)
        target = list(map(int, joltage_str.split(",")))
    else:
        target = []

    return (buttons, target)


def solve_with_z3(buttons: list[Button], target: list[int]) -> int:
    """
    Solves the machine using Z3 optimization.
    Returns minimum number of button presses.
    """
    # Number of buttons
    n_buttons = len(buttons)

    # Create Z3 integer variables for each button press count
    x = [Int(f"x{i}") for i in range(n_buttons)]

    # Create optimizer
    opt = Optimize()

    # Add constraints for each target counter
    for counter_idx, target_value in enumerate(target):
        # Sum of presses for buttons that affect this counter
        affecting_buttons_sum = Sum(
            [x[btn_idx] for btn_idx, btn in enumerate(buttons) if counter_idx in btn]
        )
        opt.add(affecting_buttons_sum == target_value)

    # All press counts must be non-negative integers
    for xi in x:
        opt.add(xi >= 0)

    # Objective: minimize total number of presses
    total_presses = Sum(x)
    opt.minimize(total_presses)

    # Solve
    if opt.check() == sat:
        model = opt.model()
        total_value: int = model.eval(total_presses).as_long()

        # Optional: get the actual solution counts
        solution = [model[xi].as_long() for xi in x]
        print(f" Solution: {solution}")  # Uncomment to see exact counts

        return total_value
    else:
        print("No solution found!")
        return 0


def main():
    # fname = "example.txt"
    fname = "input.txt"

    with open(fname) as f:
        lines = f.readlines()

    total = 0
    for line_num, line in enumerate(lines, start=1):
        line = line.strip()

        print(f"Processing line {line_num}: {line[:50]}...")

        buttons, target = parse_line(line)

        print(f" Buttons: {buttons}")
        print(f" Target: {target}")

        min_presses = solve_with_z3(buttons, target)
        print(f" Minimum presses: {min_presses}")
        print()

        total += min_presses
    #
    print(f"Total sum of minimum presses: {total}")


##############################################################################

if __name__ == "__main__":
    main()
