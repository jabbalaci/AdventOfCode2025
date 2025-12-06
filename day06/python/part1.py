#!/usr/bin/env python3

import math

import helper

# ----------------------------------------------------------------------------


class Solver:
    def __init__(self, fname: str) -> None:
        self.matrix: list[list[str]] = self.read_input(fname)
        self.columns: list[list[str]] = self.convert_matrix()

    def convert_matrix(self):
        result: list[list[str]] = []
        #
        for j in range(len(self.matrix[0])):
            col: list[str] = []
            for i in range(len(self.matrix)):
                col.append(self.matrix[i][j])
            #
            result.append(col)
        #
        return result

    def read_input(self, fname: str) -> list[list[str]]:
        return [line.split() for line in helper.read_lines(fname)]

    def start(self):
        total = 0
        for line in self.columns:
            op = line[-1]
            numbers = [int(n) for n in line[:-1]]
            if op == "+":
                value = sum(numbers)
            else:  # if op == "*":
                value = math.prod(numbers)
            #
            total += value
        #
        print(total)

    def debug(self):
        print(self.columns)


# ----------------------------------------------------------------------------


def main() -> None:
    # fname = "example.txt"
    fname = "input.txt"

    sol = Solver(fname)
    # sol.debug()
    sol.start()


##############################################################################

if __name__ == "__main__":
    main()
