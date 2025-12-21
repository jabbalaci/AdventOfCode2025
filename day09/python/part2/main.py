#!/usr/bin/env python3

from typing import NamedTuple

import matplotlib.pyplot as plt

import helper


class Point(NamedTuple):
    x: int
    y: int


def read_points(fname: str) -> list[Point]:
    lines: list[str] = helper.read_lines(fname)
    result: list[Point] = []
    #
    for line in lines:
        x, y = line.split(",")
        result.append(Point(int(x), int(y)))
    #
    result.append(result[0])
    return result


def main():
    # fname = "example.txt"
    fname = "input.txt"
    points = read_points(fname)

    # kiemelt pont (piros)
    highlight = (5984, 68669)

    xs, ys = zip(*points)

    # Y tengely megfordítása
    max_y = max(ys)
    ys_flipped = [max_y - y for y in ys]

    width_px = 10_000
    height_px = 10_000

    # width_px = 10_000
    # height_px = 10_000
    dpi = 100

    fig = plt.figure(figsize=(width_px / dpi, height_px / dpi), dpi=dpi)
    ax = fig.add_subplot(111)

    # Pontok és összekötő vonalak
    ax.plot(xs, ys_flipped, marker="o", linewidth=2)

    # Rács és tengelyek
    ax.set_aspect("equal")
    ax.grid(True)

    # Határok egy kis margóval
    margin = 10
    ax.set_xlim(min(xs) - margin, max(xs) + margin)
    ax.set_ylim(min(ys_flipped) - margin, max(ys_flipped) + margin)

    # Tengelyek eltüntetése
    ax.axis("off")

    hx, hy = highlight
    hy_flipped = max_y - hy
    ax.scatter(
        [hx],
        [hy_flipped],
        color="red",
        s=100,  # pont mérete
        zorder=10,  # biztos felül legyen
    )
    # PNG mentése
    plt.savefig("pacman.png", bbox_inches="tight", pad_inches=0.5)
    plt.close()
    print("done")


##############################################################################

if __name__ == "__main__":
    main()
