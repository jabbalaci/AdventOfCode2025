#!/usr/bin/env rdmd

import std.algorithm;
import std.array;
import std.conv;
import std.file;
import std.stdio;
import std.string;

import advent : getDivisors;

string[] grouper(const string s, const int n)
{
    string[] result;
    int steps = cast(int) s.length / n;

    int index = 0;
    foreach (i; 0 .. steps)
    {
        result ~= s[index .. index + n];
        index += n;
    }

    return result;
}

bool all_the_same(const string[] groups)
{
    assert(groups.length >= 2);
    //
    for (int i = 0; i < groups.length - 1; ++i)
    {
        if (groups[i] != groups[i + 1])
        {
            return false;
        }
    }
    return true;
}

bool has_repeated_sequence(string s)
{
    if (s.length < 2)
    {
        return false;
    }
    // else
    auto divs = getDivisors(cast(int) s.length, true); // get proper divisors
    foreach (div; divs)
    {
        string[] groups = grouper(s, div);
        if (all_the_same(groups))
        {
            return true;
        }
    }
    return false;
}

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
            if (has_repeated_sequence(s))
            {
                total += n;
            }
        }
    }
    writeln(total);
}
