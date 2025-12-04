module advent;

import std.algorithm;
import std.array;
import std.conv;
import std.file;
import std.range;
import std.stdio;
import std.string;

// read the whole content of the file (Python: f.read())
string read(const string fname, const bool trim = false)
{
    string result = readText(fname);
    if (trim)
    {
        result = result.chomp();
    }
    return result;
}

// read lines to a list of strings
string[] readLines(const string fname)
{
    return readText(fname).chomp().splitLines();
}

// read lines to a list of integers
int[] readLinesAsInts(const string fname)
{
    return readLines(fname).map!(l => l.to!int).array;
}

// for debugging (for ex. to advance a loop step by step)
string input(const string msg = "")
{
    write(msg);
    // chomp() removes the trailing newline
    return readln().chomp();
}

/*
 * Converts a number to its digits.
 * Example: 2025 -> [2, 0, 2, 5]
 * By default, it keeps the original order of the digits.
 * If the order is not important, you can set `normalOrder` to be false,
 * and then the function will be a bit faster. In this case, the order
 * is reversed: 2025 -> [5, 2, 0, 2]
*/
int[] toDigits(const long x, bool normalOrder = true) pure
{
    int[] result;
    long n = x;

    if (n == 0)
    {
        result ~= 0;
    }

    while (n)
    {
        result ~= n % 10;
        n /= 10;
    }

    if (normalOrder)
    {
        result.reverse; // keep the original order of digits (optional)
    }
    return result;
}

/*
 * Convert a string (containing a number) to a list of digits.
 * Example: "2025" -> [2, 0, 2, 5]
*/
int[] toDigits(const string s) pure
{
    import std.ascii;

    assert(s.all!(isDigit));
    //
    return s.map!(c => int(c - '0')).array;
}

/*
 * Convert a string to md5 hexa string.
 * Ex.: "test" -> "098f6bcd4621d373cade4e832627b4f6"
 */
string md5Hex(const string s) pure
{
    import std.digest.md : md5Of;
    import std.format : format;

    return format("%(%02x%)", md5Of(s));
}

// Python-like modulo
// `a` and `b` can be positive/negative, it behaves exactly like Python
int modulo(const int a, const int b) pure
{
    return ((a % b) + b) % b;
}

/*
 * Returns the divisors of a number.
 * Example: getDivisors(28)              -> [1, 2, 4, 7, 14, 28]
 *          getDivisors(28, proper=true) -> [1, 2, 4, 7, 14]
*/
int[] getDivisors(const int n, const bool proper = false) pure
{
    assert(n >= 1);
    //
    int[] result;

    foreach (i; 1 .. (n / 2) + 1)
    {
        if (n % i == 0)
        {
            result ~= i;
        }
    }
    if (!proper)
    {
        result ~= n; // n can be divided by itself
    }

    return result;
}

/*
 * Create fixed-sized groups in a string.
 * Ex.: grouper("1234", 1)   -> ["1", "2", "3", "4"]
 *      grouper("1234", 2)   -> ["12", "34"]
 *      grouper("123456", 3) -> ["123", "456"]
 */
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
