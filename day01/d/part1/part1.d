#!/usr/bin/env rdmd

import std.conv;
import std.file;
import std.stdio;
import std.string;

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
        int steps = line[1 .. $].to!int;
        for (int i = 0; i < steps; ++i)
        {
            if (dir == 'L')
            {
                --value;
                if (value < 0)
                {
                    value = 99;
                }
            }
            else // if dir == 'R'
            {
                ++value;
                if (value > 99)
                {
                    value = 0;
                }
            }
        }
        if (value == 0)
        {
            ++zeros;
        }
    } // process lines
    writeln(zeros);
}
