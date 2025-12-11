Notes for Day 11
================

Part 1
------
It was easy.


Part 2
------
It was tricky :)

In Part 1, I used breadth-first search, but it didn't work here.
It consumed too much memory. My 32 GB RAM was filled in no time.

I made some visualization (see `graph_input.jpg`) that helped a lot.

My solution is tailored to my input. My solution is not general to
any input!

I had two ideas here:

1) Instead of breadth-first search, switch to depth-first search.
   It solved the memory issue immediately.

2) The problem was too big. Going from from `svr` to `out` was too much.
   But, we knew that we had to reach two nodes: `fft` and `dac`.
   In my input, the order was the following: `svr -> fft -> dac -> out`.
   So, instead of doing `svr -> out`, I split up the problem to smaller pieces:

   `svr -> fft`

   `fft -> dac`

   `dac -> out`

   The numbers I get for each piece must be multiplied together to get the final result.

   Visualization showed me that I can stop early. For instance, if I
   work on `svr -> fft`, then there are 4 nodes
   that come after `fft`: `["lfr", "xsh", "vfm", "dhl"]`.
   These are stop nodes: if I reach any of them, I can stop.

   Similarly, if I go from `fft` to `dac`,
   there are again some stop nodes: `["dev", "oki", "gbd", "npt", "you"]`.

   `fft -> dac` is the longest part, its calculation took most of the time.

---

Run Part 2 with PyPy. It's much faster.
