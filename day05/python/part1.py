#!/usr/bin/env python3

import helper


def included(value: int, ranges: list[range]) -> bool:
    for r in ranges:
        if value in r:
            return True
        #
    #
    return False


def main() -> None:
    # parts: list[str] = helper.read("example.txt").strip().split("\n\n")
    parts: list[str] = helper.read("input.txt").strip().split("\n\n")

    # 1st part
    ranges: list[range] = []
    for line in parts[0].splitlines():
        pieces = line.split("-")
        a = int(pieces[0])
        b = int(pieces[1])
        ranges.append(range(a, b + 1))
    #

    # 2nd part
    fresh = 0
    for line in parts[1].splitlines():
        value = int(line)
        if included(value, ranges):
            fresh += 1
        #
    #
    print(fresh)


##############################################################################

if __name__ == "__main__":
    main()
