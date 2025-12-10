#!/usr/bin/env python3

import sys
from collections import deque

import helper

# Default limit: 1000. It was not enough.
# With trial and error I found 1008 to work for my input but I set the limit higher to be sure.
sys.setrecursionlimit(1100)

Button = tuple[int, ...]

# ----------------------------------------------------------------------------


class Machine:
    def __init__(self, line: str) -> None:
        parts = line.split()
        parts.pop()  # we don't need the last part (joltage requirement)
        first = parts.pop(0)  # indicator
        first = first.replace(".", "0").replace("#", "1").replace("[", "").replace("]", "")
        # goal position:
        self.indicator = [int(digit) for digit in first]
        self.buttons: list[Button] = []
        for part in parts:
            part = part.replace("(", "").replace(")", "")
            button = tuple([int(n) for n in part.split(",")])
            self.buttons.append(button)
        #
        self.q: deque[tuple[list[int], int]] = deque()
        self.elems_in_queue: set[Button] = set()

    def show(self) -> None:
        print(self.indicator, end="; ")
        print(self.buttons)

    def extend(self, elem: tuple[list[int], int]) -> int:
        state = elem[0]
        depth = elem[1]
        if state == self.indicator:
            return depth
        # else
        for button in self.buttons:
            copy = state.copy()
            for idx in button:
                copy[idx] = 1 - copy[idx]  # toggle
            #
            self.add_to_queue((copy, depth + 1))
        #
        return self.extend(self.q.popleft())

    def add_to_queue(self, elem: tuple[list[int], int]) -> None:
        # If an elem is/was in the queue, don't add it again.
        state = tuple(elem[0])
        if state not in self.elems_in_queue:
            self.q.append(elem)
            self.elems_in_queue.add(state)

    def start(self) -> int:
        initial_state = [0] * len(self.indicator)
        self.add_to_queue((initial_state, 0))
        result = self.extend(self.q.popleft())
        return result


# ----------------------------------------------------------------------------


def main() -> None:
    # fname = "example.txt"
    fname = "input.txt"

    lines: list[str] = helper.read_lines(fname)
    total = 0
    for line in lines:
        m = Machine(line)
        # m.show()
        total += m.start()
    #
    print(total)


##############################################################################

if __name__ == "__main__":
    # print(sys.getrecursionlimit())
    main()
