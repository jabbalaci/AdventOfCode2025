Part 2
======

Here I got some help from Mocsa. Thanks!

We solved it with visualization. We didn't write a program for this.

See `part2.png`. The polygon is similar to a PacMan. There's a horizontal
area at the middle of the polygon, let's call it the "mouth" of PacMan.

After investigating the polygon, it was clear that one of the points
must be at the mouth on the right side. The solution (rectangle)
must be either above or below the mouth.

In my case, the solution was below the mouth. I opened the PNG in Gimp
and marked point A. I drew a line downwards and got point B. Then
drew a line to the left direction. It intersected a horizontal line.
I went up to the first point. However, this is not the second point!
You can move left, getting point C. This is the second point of the
rectangle we are looking for. The points A and C are the opposite points
of the rectangle.

I also checked above the mouth of the PacMan, but the rectangle I got there
was smaller.

The two points in my case:

A(x=94581, y=50187)
C(x=5984,  y=68669)

>>> x = 94581-5984+1
>>> y = 68669-50187+1
>>> x*y
1637556834

It would be nice to solve this exercise with a program.
