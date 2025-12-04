#!/usr/bin/env rdmd

import std.algorithm;
import std.file;
import std.stdio;
import std.string;

import advent : toDigits;

int process(const string line)
{
    int[] digits = toDigits(line);
    int window = cast(int) digits.length - 1;
    int a = digits[0 .. window].maxElement;
    int idx = cast(int) digits.countUntil(a);
    int b = digits[idx + 1 .. $].maxElement;

    return a * 10 + b;
}

void main()
{
    // const fname = "example.txt";
    const fname = "input.txt";

    const lines = readText(fname).splitLines;

    int total = 0;
    foreach (line; lines)
    {
        total += process(line);
    }
    writeln(total);
}
