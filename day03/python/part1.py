#!/usr/bin/env python3

import helper

def get_max_joltage(line: str) -> int:
    numbers: list[int] = [int(c) for c in line]
    first = max(numbers)
    first_pos = numbers.index(first)
    if first_pos < len(numbers) - 1:  # method A
        second = max(numbers[first_pos+1:])
        return first * 10 + second
    else:  # method B
        second = max(numbers[:first_pos])
        return second * 10 + first

def main() -> None:
    # lines: list[str] = helper.read_lines("example.txt")
    lines: list[str] = helper.read_lines("input.txt")

    total = 0
    for line in lines:
        # print(line)
        value = get_max_joltage(line)
        # print("#", value)
        total += value
    #
    print(total)


##############################################################################

if __name__ == "__main__":
    main()
