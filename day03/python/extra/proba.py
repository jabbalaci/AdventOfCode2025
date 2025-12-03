#!/usr/bin/env python3

# Some tests for Part 2 to better understand the problem.

import itertools

import helper


def get_max_joltage(line: str) -> int:
    numbers: list[int] = [int(c) for c in line]
    first = max(numbers)
    first_pos = numbers.index(first)
    if first_pos < len(numbers) - 1:  # method A
        second = max(numbers[first_pos + 1 :])
        return first * 10 + second
    else:  # method B
        second = max(numbers[:first_pos])
        return second * 10 + first


def get_max_joltage_v2(line: str) -> int:
    digits: list[int] = [int(c) for c in line]
    pairs = list(enumerate(digits))
    maxi = -1
    save = None
    for pairs in itertools.combinations(pairs, 11):
        rev = pairs[::-1]
        value = 0
        for i in range(len(pairs)):
            value += rev[i][-1] * (10**i)
        if value > maxi:
            maxi = value
            save = pairs
    #
    print("#", save)
    #
    return maxi


def main() -> None:
    lines: list[str] = helper.read_lines("example.txt")
    # lines: list[str] = helper.read_lines("input.txt")

    total = 0
    for line in lines:
        print(line)
        # value = get_max_joltage(line)
        value = get_max_joltage_v2(line)
        print("#", value)
        print("---")
        total += value
    #
    print("===")
    print(total)


##############################################################################

if __name__ == "__main__":
    main()
