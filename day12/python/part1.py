#!/usr/bin/env python3

import helper

N = 3


def test(width: int, height: int, total: int) -> bool:
    a = width // N
    b = height // N
    return a * b >= total


def main() -> None:
    lines: list[str] = [line for line in helper.read_lines("input.txt") if "x" in line]

    result = 0
    for line in lines:
        left, right = line.split(":")
        w, h = left.split("x")
        width = int(w)
        height = int(h)
        total = sum(int(n) for n in right.split())
        ok = test(width, height, total)
        if ok:
            result += 1
        #
    #
    print(result)


##############################################################################

if __name__ == "__main__":
    main()
