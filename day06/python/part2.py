#!/usr/bin/env python3

import math

import helper

char = str

OUTSIDE, INSIDE = range(2)

# ----------------------------------------------------------------------------


class Line:
    def __init__(self, line: str) -> None:
        self.line: str = line
        self.idx = 0
        self.last_token = ""

    def next_token(self) -> str:
        result = ""
        state = OUTSIDE
        #
        while True:
            if self.idx == len(self.line):
                # we reached the end of the line
                state = OUTSIDE
                break
            if (state == INSIDE) and (self.line[self.idx] == " "):
                state = OUTSIDE
                break
            # else
            c = self.line[self.idx]
            self.idx += 1
            result += c
            if c != " ":
                state = INSIDE
            #
        #
        self.last_token = result
        return result

    def equalize_cursor(self, width: int) -> None:
        steps = width - len(self.last_token)
        self.idx += steps

    def move_cursor(self) -> None:
        self.idx += 1


# ----------------------------------------------------------------------------


class Solver:
    def __init__(self, fname: str) -> None:
        lines: list[str] = helper.read_lines(fname)
        self.operators = lines.pop().split()
        self.number_of_lines = len(lines)  # lines with numbers
        self.number_of_cols = len(self.operators)
        self.my_lines: list[Line] = [Line(line) for line in lines]

    def read_tokens(self) -> list[str]:
        result: list[str] = []
        for line in self.my_lines:
            result.append(line.next_token())
        #
        return result

    def equalize_cursors(self, width: int) -> None:
        for line in self.my_lines:
            line.equalize_cursor(width)

    def move_cursors(self) -> None:
        for line in self.my_lines:
            line.move_cursor()

    def evaluate(self, tokens: list[str], op: char) -> int:
        numbers: list[int] = []
        for i in range(len(tokens[0])):
            s = ""
            for tok in tokens:
                s += tok[i]
            #
            numbers.append(int(s))
        #
        if op == "+":
            return sum(numbers)
        else:
            return math.prod(numbers)

    def start(self) -> None:
        total = 0
        for i in range(self.number_of_cols):
            if i > 0:
                self.move_cursors()
            #
            tokens = self.read_tokens()
            longest_token = max(len(tok) for tok in tokens)
            self.equalize_cursors(longest_token)
            tokens = [tok + (" " * (longest_token - len(tok))) for tok in tokens]
            print(tokens, self.operators[i])
            total += self.evaluate(tokens, self.operators[i])
        #
        print(total)

    def debug(self) -> None:
        for line in self.my_lines:
            print(line.idx)


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
