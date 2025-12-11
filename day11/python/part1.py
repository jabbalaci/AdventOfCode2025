#!/usr/bin/env python3

from collections import deque
from pprint import pprint

import helper

# ----------------------------------------------------------------------------


class Graph:
    def __init__(self, fname: str) -> None:
        self.d: dict[str, list[str]] = self.read_input(fname)

    def read_input(self, fname: str) -> dict[str, list[str]]:
        d: dict[str, list[str]] = {}
        lines: list[str] = helper.read_lines(fname)
        #
        for line in lines:
            left, right = line.split(":")
            d[left] = right.split()
        #
        return d

    def start(self, node1: str, node2: str) -> None:
        # we want to go from node1 to node2
        counter = 0
        q: deque[list[str]] = deque()
        q.append([node1])
        while q:
            elem = q.popleft()
            end = elem[-1]
            if end == node2:
                counter += 1
            else:
                for child in self.d[end]:
                    q.append(elem + [child])
                #
            #
        #
        print(counter)

    def show(self) -> None:
        pprint(self.d)


# ----------------------------------------------------------------------------


def main() -> None:
    # fname = "example.txt"
    fname = "input.txt"

    g = Graph(fname)
    # g.show()
    g.start("you", "out")


##############################################################################

if __name__ == "__main__":
    main()
