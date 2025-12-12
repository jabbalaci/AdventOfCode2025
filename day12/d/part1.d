#!/usr/bin/env rdmd

import std.algorithm;
import std.array;
import std.conv;
import std.file;
import std.stdio;
import std.string;

enum N = 3;

bool test(const int width, const int height, const int total) pure
{
    int a = width / 3;
    int b = height / 3;
    return a * b >= total;
}

void main()
{
    const lines = readText("input.txt").splitLines.filter!(line => line.canFind('x')).array;

    int result = 0;
    foreach (line; lines)
    {
        auto parts = line.split(':');
        auto left = parts[0];
        auto right = parts[1];
        auto pieces = left.split('x');
        int width = pieces[0].to!int;
        int height = pieces[1].to!int;
        int total = right.split.map!(to!int).sum;
        if (test(width, height, total))
        {
            ++result;
        }
    }
    writeln(result);
}
