#!/usr/bin/env python3

# Thanks Mocsa for the help!

import helper

Pair = tuple[int, int]


def read_input_file(fname: str) -> list[Pair]:
    first_part: str = helper.read(fname).split("\n\n")[0]
    d: dict[int, int] = {}
    for line in first_part.splitlines():
        pieces = line.split("-")
        a = int(pieces[0])
        b = int(pieces[1])
        old_value = d.get(a, 0)
        if b > old_value:
            d[a] = b
        #
    #
    return sorted(d.items())


def main() -> None:
    # fname = "example.txt"  # 14
    # fname = "example2.txt"  # 10
    fname = "input.txt"

    intervals: list[Pair] = read_input_file(fname)
    mini = intervals[0][0]
    maxi = intervals[-1][1]
    all_values = maxi - mini + 1

    total = 0
    end = intervals[0][1]
    for i in range(0, len(intervals) - 1):
        curr = intervals[i]
        next = intervals[i + 1]
        end = max(end, curr[1])
        start = next[0]
        if (diff := start - end - 1) > 0:
            total += diff
    #
    print(all_values - total)


##############################################################################

if __name__ == "__main__":
    main()
