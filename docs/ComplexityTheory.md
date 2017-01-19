Complexity Theory
=================

## Overview
* Space complexity: how much memory an algorithm needs
* Time complexity: how much time an algorithm needs
* Generally, we don't care as much about space complexity because memory is so cheap

## How to Measure Time Complexity?
* Differences in environments make it difficult to measure absolute time
    * A new computer is faster than an old computer
    * Super computer is more powerful than a smartphone
* Solution: we consider the number of steps because it is generic and machine independent
* Important: we want to make a good guess about how the algorithm's running time depends on
the number of items (input size).  
* The order of growth: how the algorithm will scale and behave with the input size
* Good algorithms are deterministic and approximately linear
* Asymptotic analysis: determining how an algorithm's performance changes with large input sizes

## Linear vs. Quadratic Sort Algorithm Example

| # items | 1st Algorithm O(n) | 2nd Algorithm O(n^2) |
-------------------------------------------------------
|   10    |     1 ms           |    1 ms              |
-------------------------------------------------------
|   20    |     2 ms           |    4 ms              |
-------------------------------------------------------
|   100   |     10 ms          |    100 ms            |
-------------------------------------------------------

## Complexity Notations
* Big Ordo Notation
* Big Theta Notation
* Big Omega Notation

## Algorithm Running Times (from best to worst)
* O(1) - Constant
* O(logN) - Logarithmic
* O(N) - Linear
* O(N*logN) - Linearithmic
* O(N^k) - Polynomial (k > 1)
* O(N^n) - Exponential (c is constant)
* O(N!) - Factorial

## Complexity Classes
* P: Polynomial - problems are efficiently solvable but not all have practical solutions
* NP: Non-deterministic Polynomial - solutions can be verified in polynomial time
* NP Complete
* NP Hard

## Complexity Case Studies
* Linear search on an array => O(N)
* Binary search on a sorted array => O(logN)
* Bubble sort => O(N^2)
