#!/usr/bin/env rdmd

import std.conv;
import std.file;
import std.stdio;
import std.string;

void main()
{
    // const fname = "example.txt";
    const fname = "input.txt";

    const line = readText(fname).chomp;
    const parts = line.split(",");

    long total = 0;
    foreach (part; parts)
    {
        auto pieces = part.split("-");
        long a = pieces[0].to!long;
        long b = pieces[1].to!long;

        foreach (n; a .. b + 1)
        {
            string s = n.to!string;
            if (s.length % 2 == 0)
            {
                auto half = s.length / 2;
                if (s[0 .. half] == s[half .. $])
                {
                    total += n;
                }
            }
        }
    }
    writeln(total);
}
