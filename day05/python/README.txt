How to solve Part 2?
====================

It was tricky.

We have intervals.
First, I built a dictionary where the key was the first value (start of the interval),
and the value was the second value (end of the interval).
In the input, the start of the interval can be present several times!
So pay attention not to overwrite the key's corresponding value.
When you find a value that is larger than the stored value, you can update the dictionary.

Example:

3-4
3-5        # larger end value for an existing key: update the dict
10-14
16-20
12-18

Dictionary:

3: 5
10: 14
16: 20
12: 18

Make a list of tuples and sort it:

[(3, 5), (10, 14), (12, 18), (16, 20)]

Now we have the intervals in a comfortable format.

Question: how many elements are *inside* the intervals?

But, it's easier to answer the opposite: how many elements are OUTSIDE of the intervals?

We know that the smallest value is 3, the largest is 20. In (3, 20), there
are 18 elements (20 - 3 + 1).
In this example, if you draw it on a paper, you can see that 4 elements are outside.
Thus, 18 - 4 = 14 elements must be inside.

How to figure out the number of elements that are outside?

3, 5
10, 14
12, 18
16, 20

Take the end of an interval (here: 5) and the beginning of the next interval (here: 10).
There are 10 - 5 - 1 = 4 elements between them (namely: 6, 7, 8, 9).
12 - 14 is negative: drop it
16 - 18: drop it

There's a special case though:

3-5
4-4
8-9
16-20

They are nicely ordered and the beginning of an interval is less than or equal to the
end of the interval. Seems good.

Let's draw it:

[3 [4] 5] 6 7 [8 9] 10 11 12 13 14 15 [16 17 18 19 20]

Problem:

4 minus 5: negative, drop it
8 minus 4 is 4, so we might say that we have 5, 6, and 7 outside, i.e. between 4 and 8.
However, you cannot count 5 because it's part of the (3, 5) interval! 5 is inside an interval!

Solution:

In a variable, store the largest end value. Here, its initial value is 5.
Then, when you find a larger end value, update it. But if the end value is smaller,
DON'T update it!

This way, you can find the correct answer.
