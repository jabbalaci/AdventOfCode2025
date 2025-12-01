#!/usr/bin/env rdmd

// improved version using modulo

import std.conv;
import std.file;
import std.stdio;
import std.string;

// Python-like modulo
// `a` and `b` can be positive/negative, it behaves exactly like Python
int modulo(const int a, const int b) pure
{
    return ((a % b) + b) % b;
}

void main()
{
    // const fname = "example.txt";
    const fname = "input.txt";

    const lines = readText(fname).splitLines;
    int value = 50;
    int zeros = 0;

    foreach (line; lines)
    {
        char dir = line[0];
        int steps = line[1 .. $].to!int * ((dir == 'L') ? -1 : +1);

        value += steps;
        value = value.modulo(100);

        if (value == 0)
        {
            ++zeros;
        }
    }

    writeln(zeros);
}
