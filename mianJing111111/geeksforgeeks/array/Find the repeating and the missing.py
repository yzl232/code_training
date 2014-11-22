# encoding=utf-8
'''
Given an unsorted array of size n. Array elements are in range from 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in array. Find these two numbers.

Examples:

  arr[] = {3, 1, 3}
  Output: 2, 3   // 2 is missing and 3 occurs twice

  arr[] = {4, 3, 6, 2, 1, 1}
  Output: 1, 5  // 5 is missing and 1 occurs twice


Method 4 (Make two equations)
Let x be the missing and y be the repeating element.

1) Get sum of all numbers.
Sum of array computed S = n(n+1)/2 – x + y
2) Get product of all numbers.
Product of array computed P = 1*2*3*…*n * y / x
3) The above two steps give us two equations, we can solve the equations and get the values of x and y.

Time Complexity: O(n)

另外用sort之后也可以做。
'''