#!/usr/bin/env python3

"""
It works with the example but it cannot solve the real input.
The recursion is too deep and it dies.

We need a different approach. People suggested the Z3 theorem prover.
"""

import sys
from collections import deque

import helper

# Default limit: 1000. It was not enough.
sys.setrecursionlimit(1_000_000)

Button = tuple[int, ...]

# ----------------------------------------------------------------------------


class Machine:
    def __init__(self, line: str) -> None:
        parts = line.split()
        last_part = parts.pop().replace("{", "").replace("}", "")  # joltage requirement
        parts.pop(0)  # indicator is not needed -> remove it
        # goal position:
        self.goal = [int(n) for n in last_part.split(",")]
        self.buttons: list[Button] = []
        for part in parts:
            part = part.replace("(", "").replace(")", "")
            button = tuple([int(n) for n in part.split(",")])
            self.buttons.append(button)
        #
        self.q: deque[tuple[list[int], int]] = deque()
        self.elems_in_queue: set[Button] = set()

    def extend(self, elem: tuple[list[int], int]) -> int:
        state = elem[0]
        depth = elem[1]
        if state == self.goal:
            return depth
        # else
        for button in self.buttons:
            good = True
            copy = state.copy()
            for idx in button:
                copy[idx] += 1
                if copy[idx] > self.goal[idx]:
                    good = False
                    break
                #
            #
            if good:
                self.add_to_queue((copy, depth + 1))
        #
        return self.extend(self.q.popleft())

    def add_to_queue(self, elem: tuple[list[int], int]) -> None:
        # If an elem is/was in the queue, don't add it again.
        state = tuple(elem[0])
        if state not in self.elems_in_queue:
            self.q.append(elem)
            self.elems_in_queue.add(state)

    def show(self) -> None:
        print(self.buttons, end="; ")
        print(self.goal)

    def start(self) -> int:
        self.show()
        initial_state = [0] * len(self.goal)
        self.add_to_queue((initial_state, 0))
        result = self.extend(self.q.popleft())
        print(result)
        return result


# ----------------------------------------------------------------------------


def main() -> None:
    # fname = "example.txt"
    # fname = "input.txt"
    fname = "sorted.txt"

    lines: list[str] = helper.read_lines(fname)
    total = 0
    for line in lines:
        m = Machine(line)
        # m.show()
        total += m.start()
        print("---")
    #
    print(total)


##############################################################################

if __name__ == "__main__":
    # print(sys.getrecursionlimit())
    main()
