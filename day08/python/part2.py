#!/usr/bin/env python3

import math
from pprint import pprint
from typing import NamedTuple

import helper


class Point(NamedTuple):
    x: int
    y: int
    z: int


# ----------------------------------------------------------------------------


class Connection:
    def __init__(self) -> None:
        self.boxes: list[set[Point]] = []

    def find(self, p: Point):
        for idx, box in enumerate(self.boxes):
            if p in box:
                return idx
            #
        #
        return -1

    def add(self, a: Point, b: Point):
        i = self.find(a)
        j = self.find(b)
        # if neither of the was found:
        if (i == -1) and (j == -1):
            self.boxes.append(set([a, b]))
            return
        # else
        if (i > -1) and (j > -1):
            # if both are found
            if i == j:
                # if they are in the same box -> nothing to do
                return
            # if they are in different boxes: merge them
            for p in self.boxes[j]:
                self.boxes[i].add(p)
            #
            del self.boxes[j]
            return
        # else, just one of them is found
        if i > -1:
            self.boxes[i].add(b)
            return
        if j > -1:
            self.boxes[j].add(a)
            return
        # else
        assert False, "We should never get here."

    def show(self) -> None:
        for box in self.boxes:
            print(box)


# ----------------------------------------------------------------------------


def distance_between(a: Point, b: Point) -> float:
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)


def distance_from_origo(p: Point) -> int:
    return p.x + p.y + p.z


class Solver:
    def __init__(self, fname: str) -> None:
        self.data: list[Point] = self.read_input(fname)
        self.number_of_points = len(self.data)
        self.connection = Connection()
        # self.points: list[Point] = []

    def read_input(self, fname: str) -> list[Point]:
        result: list[Point] = []
        lines: list[str] = helper.read_lines(fname)
        #
        for line in lines:
            a, b, c = line.split(",")
            result.append(Point(int(a), int(b), int(c)))
        #
        return result

    def find_distances(self) -> dict[float, tuple[Point, Point]]:
        d: dict[float, tuple[Point, Point]] = {}
        for i in range(len(self.data) - 1):
            for j in range(i + 1, len(self.data)):
                first: Point = self.data[i]
                second: Point = self.data[j]
                dist = distance_between(first, second)
                # d[(first, second)] = dist
                assert dist not in d
                d[dist] = tuple(sorted([first, second], key=distance_from_origo))  # type: ignore
            #
        #
        d2 = {}
        for k in sorted(d.keys()):
            d2[k] = d[k]
        #
        return d2

    def start(self) -> None:
        d: dict[float, tuple[Point, Point]] = self.find_distances()
        # pprint(d)
        # print("---")
        counter = 0
        for a, b in d.values():
            self.connection.add(a, b)
            counter += 1
            if (
                len(self.connection.boxes) == 1
                and len(self.connection.boxes[0]) == self.number_of_points
            ):
                break
        #
        # print(a, b)
        # print("---")
        result = a[0] * b[0]
        print(result)

    def show(self) -> None:
        for p in self.data:
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
