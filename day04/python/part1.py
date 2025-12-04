#!/usr/bin/env python3

import sys

import helper

# ----------------------------------------------------------------------------

char = str

GridType = list[list[char]]


# ----------------------------------------------------------------------------


class Grid:
    def __init__(self, fname: str) -> None:
        self.matrix: GridType = [list(line) for line in helper.read_lines(fname)]

    def get_cell_value(self, i: int, j: int, default=".") -> char:
        if (i < 0) or (j < 0):
            return default  # type: ignore
        try:
            return self.matrix[i][j]
        except IndexError:
            return default  # type: ignore

    def get_all_neighbors(self, i: int, j: int) -> list[char]:
        result = []
        positions = [
            (i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j - 1),
            (i + 1, j),
            (i + 1, j + 1),
        ]
        for a, b in positions:
            result.append(self.get_cell_value(a, b))
        return result

    def start(self) -> None:
        total = 0
        for i, row in enumerate(self.matrix):
            for j, c in enumerate(row):
                if c == "@":
                    neighbors: list[char] = self.get_all_neighbors(i, j)
                    if neighbors.count("@") < 4:
                        total += 1
                    #
                #
            #
        #
        print(total)

    def show(self) -> None:
        for i, row in enumerate(self.matrix):
            for j, c in enumerate(row):
                sys.stdout.write(c)
            #
            print()
        #


# ----------------------------------------------------------------------------


def main() -> None:
    # fname = "example.txt"
    fname = "input.txt"

    g = Grid(fname)
    # g.show()
    g.start()


##############################################################################

if __name__ == "__main__":
    main()
