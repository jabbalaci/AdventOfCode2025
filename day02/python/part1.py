#!/usr/bin/env python3

import helper


def main() -> None:
    # line: str = helper.read("example.txt", trim=True)
    line: str = helper.read("input.txt", trim=True)

    parts: list[str] = line.split(",")
    parts.sort(key=lambda l: int(l.split("-")[0]))

    total = 0
    for part in parts:
        pieces: list[str] = part.split("-")
        a = int(pieces[0])
        b = int(pieces[1])
        for n in range(a, b+1):
            s = str(n)
            if len(s) % 2 == 0:
                half = len(s) // 2
                if s[:half] == s[half:]:
                    # print("#", n)
                    total += n
                #
            #
        #
    #
    print(total)


##############################################################################

if __name__ == "__main__":
    main()
