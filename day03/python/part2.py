#!/usr/bin/env python3

import helper

STEPS = 12


class Digit:
    def __init__(self, idx: int, value: int) -> None:
        self.idx = idx
        self.value = value
        self.used = False

    def __str__(self) -> str:
        return f"(idx: {self.idx}, {self.value}, {'+' if self.used else ''})"


class Line:
    def __init__(self, line: str) -> None:
        self.line = line
        self.digits: list[Digit] = [Digit(i, int(v)) for i, v in enumerate(line)]
        self.total = 0

    def get_used(self):
        return [d for d in self.digits if d.used]

    def get_not_used(self):
        return [d for d in self.digits if not d.used]

    def get_value_of(self, li: list[Digit]) -> int:
        li.sort(key=lambda d: d.idx)
        return int("".join([str(d.value) for d in li]))

    def get_current_value(self) -> int:
        li = self.get_used()
        if len(li) == 0:
            return 0
        # else
        return int("".join([str(d.value) for d in li]))

    def step(self) -> None:
        used = self.get_used()
        maxi = 0
        chosen = None
        for d in self.get_not_used():
            value = self.get_value_of([d] + used)
            if value > maxi:
                maxi = value
                chosen = d
            #
        #
        assert chosen
        chosen.used = True
        self.total = maxi

    def execute_steps(self, n=STEPS) -> None:
        for _ in range(n):
            self.step()

    def __str__(self) -> str:
        sb = "["
        for digit in self.digits:
            sb += str(digit)
            sb += ", "
        sb += "] "
        sb += f"(value: {self.get_current_value()})"
        return sb


def main() -> None:
    # lines: list[str] = helper.read_lines("example.txt")
    lines: list[str] = helper.read_lines("input.txt")

    total = 0
    for line in lines:
        curr = Line(line)
        # print(curr)
        curr.execute_steps()
        # print(curr)
        total += curr.get_current_value()
    #
    print(total)


##############################################################################

if __name__ == "__main__":
    main()
