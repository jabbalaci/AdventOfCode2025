#!/usr/bin/env python3

"""
+--> X
|
v

Y
"""

from typing import NamedTuple

import helper


class Point(NamedTuple):
    x: int
    y: int


# ----------------------------------------------------------------------------


class Solver:
    def __init__(self, fname: str) -> None:
        self.points: list[Point] = self.read_input(fname)

    def read_input(self, fname: str) -> list[Point]:
        result: list[Point] = []
        lines: list[str] = helper.read_lines(fname)
        #
        for line in lines:
            x, y = line.split(",")
            result.append(Point(int(x), int(y)))
        #
        return result

    def area(self, p1: Point, p2: Point) -> int:
        a = abs(p1.x - p2.x) + 1
        b = abs(p1.y - p2.y) + 1
        return a * b

    def start(self) -> None:
        maxi = 0
        for i in range(len(self.points) - 1):
            for j in range(i + 1, len(self.points)):
                p1 = self.points[i]
                p2 = self.points[j]
                if (value := self.area(p1, p2)) > maxi:
                    maxi = value
                #
            #
        #
        print(maxi)

    def show(self):
        for p in self.points:
            print(p)


# ----------------------------------------------------------------------------


def main() -> None:
    # fname = "example.txt"
    fname = "input.txt"

    sol = Solver(fname)
    # sol.show()
    sol.start()


##############################################################################

if __name__ == "__main__":
    main()
