#!/usr/bin/env python3

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

    def start(self, node1: str, node2: str, stop_nodes: list[str]) -> int:
        # we want to go from node1 to node2
        print(f"# {node1} -> {node2}")
        result = 0
        stack = [node1]
        while stack:
            end = stack.pop()
            if end in stop_nodes:
                continue
            #
            if end == node2:
                result += 1
            #
            else:
                for child in self.d.get(end, []):
                    stack.append(child)
                #
            #
        #
        print(result)
        return result

    def show(self) -> None:
        pprint(self.d)


# ----------------------------------------------------------------------------


def main() -> None:
    # example = True
    example = False
    if example:
        print("# example")
        g = Graph("example2.txt")
        a = g.start("svr", "fft", ["ccc"])
        b = g.start("fft", "dac", ["fff"])
        c = g.start("dac", "out", [])
        print("---")
        print("Result:", a * b * c)
    else:
        print("# real input")
        g = Graph("input.txt")
        a = g.start("svr", "fft", ["lfr", "xsh", "vfm", "dhl"])
        b = g.start("dac", "out", [])
        c = g.start("fft", "dac", ["dev", "oki", "gbd", "npt", "you"])
        print("---")
        print("Result:", a * b * c)


##############################################################################

if __name__ == "__main__":
    main()
