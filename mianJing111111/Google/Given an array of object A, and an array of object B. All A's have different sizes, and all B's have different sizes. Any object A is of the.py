# encoding=utf-8
'''
Given an array of object A, and an array of object B. All A's have
different sizes, and all B's have different sizes. Any object A is of the
same size as exactly one object B. We have a function f(A, B) to compare the
size of one A and one B. But we cannot compare between two A's or two B's.
Give an algorithm to match each A with each B.
'''


'''
This problem is basically [matchine Nuts and bolts].

Solution to this problem is with help of quicksort.
1. pick any object A randomly, then compare it all B to find the exact match for it. This pivot in quicksort.
2. While searching for match divide B into two part with respect to pivot so this will make
all small object (of type B) than pivot on left side and all large object (of type B ) on right.. same as quicksort.
3. So at this point we find exact match for B as well as we aligend B. Now we can do the same thing on array of object A . Then repeat the process for on both halves.

Complexity will be (n lg n)

Note:-
We are doing this way we cant directly compare two A type of objects.

Ref:-
[http] www wisdom weizmann ac il/~naor/PUZZLES/nuts_solution.html
'''