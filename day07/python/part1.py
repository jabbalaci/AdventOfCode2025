#!/usr/bin/env python3

import sys
from typing import NamedTuple

import helper

# ----------------------------------------------------------------------------

char = str

GridType = list[list[char]]


class Point(NamedTuple):
    row: int
    col: int


# ----------------------------------------------------------------------------


class Laser:
    def __init__(self, p: Point, parent: "Grid") -> None:
        self.parent = parent
        self.row = p.row
        self.col = p.col
        self.active = True  # alive

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        # else
        return (self.row == other.row) and (self.col == other.col)

    def __hash__(self) -> int:
        return hash((self.row, self.col))

    def move_down(self) -> list["Laser"]:
        # kill this and either a) create a new one or b) create two children
        self.active = False

        below = self.row + 1
        if below >= self.parent.number_of_rows:  # we went out of the map
            return []
        #
        c = self.parent.get_cell_value(below, self.col)
        if c == ".":
            return [Laser(Point(below, self.col), self.parent)]
        elif c == "^":
            self.parent.splits += 1
            left = Laser(Point(below, self.col - 1), self.parent)
            right = Laser(Point(below, self.col + 1), self.parent)
            return [left, right]
        else:
            assert False, "We should never get here."

    def __repr__(self) -> str:
        # return f"Laser(row: {self.row}, col: {self.col})"
        return f"Laser(human_row: {self.row + 1}, human_col: {self.col + 1})"


# ----------------------------------------------------------------------------


class Grid:
    def __init__(self, fname: str) -> None:
        self.matrix: GridType = [list(line) for line in helper.read_lines(fname)]
        self.number_of_rows = len(self.matrix)
        self.number_of_cols = len(self.matrix[0])
        self.S = Point(0, self.matrix[0].index("S"))
        self.lasers: list[Laser] = [Laser(self.S, self)]
        self.splits = 0  # count the result here

    def get_cell_value(self, i: int, j: int, default=".") -> char:
        if (i < 0) or (j < 0):
            return default  # type: ignore
        try:
            return self.matrix[i][j]
        except IndexError:
            return default  # type: ignore

    def compact_lasers(self) -> None:
        """remove duplicates"""
        self.lasers = list(set(self.lasers))

    def get_active_lasers(self):
        return [laser for laser in self.lasers if laser.active]

    def start(self) -> None:
        while True:
            active_lasers: list[Laser] = self.get_active_lasers()
            if len(active_lasers) == 0:
                break
            # else
            for laser in active_lasers:
                children: list[Laser] = laser.move_down()
                self.lasers.extend(children)
            #
            self.compact_lasers()
            # self.show()
            # input("Press ENTER to continue...")
            # if counter == 4:
            # break
            #
        #
        print(self.splits)

    def is_there_a_laser(self, row: int, col: int) -> bool:
        for laser in self.lasers:
            if (laser.row == row) and (laser.col == col):
                return True
            #
        #
        return False

    def show(self) -> None:
        for i, row in enumerate(self.matrix):
            for j, c in enumerate(row):
                if c != ".":
                    sys.stdout.write(c)
                else:
                    if self.is_there_a_laser(i, j):
                        sys.stdout.write("|")
                    else:
                        sys.stdout.write(c)
            #
            print()
        #
        print("Splits:", self.splits)
        for laser in self.get_active_lasers():
            print(laser)
        #
        print("---")


# ----------------------------------------------------------------------------


def main() -> None:
    # fname = "example.txt"
    fname = "input.txt"

    g = Grid(fname)
    g.start()

    # g.show()


##############################################################################

if __name__ == "__main__":
    main()
