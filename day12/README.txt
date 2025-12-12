Notes for Day 12
================

Eric Wastl, the creator of Advent of Code trolled us today :)

When I read the description of the problem, I said to myself:
"it's too complicated". I looked at the input and thought: "too many boxes".

But actually, the problem is very simple.

Let's take the first line of my input:

47x48: 59 59 54 61 53 61

We have an area with width 47 and height 48.
The sum of the boxes is 347.

Each box has dimension 3x3. The shape doesn't matter!
And ignore the example. You don't need to rotate and/or flip the boxes.

You start placing the boxes in the area.
When the first row is filled, you continue in the next row.
Do you have enough space for the boxes?

In this example, in a row we can put 47 / 3 = 15 boxes (integer division).
Number of rows: 48 / 3 = 16.
15 * 16 = 240. We cannot place here 347 boxes.

Repeat this procedure with every line of the input file.
