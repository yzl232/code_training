# encoding=utf-8
'''
Method 2 (A space efficient implementation)
This method efficiently utilizes the available space. It doesn’t cause an overflow if there is space available in arr[].

The idea is to start two stacks from two extreme corners of arr[]. stack1 starts from the leftmost element, the first element in stack1 is pushed at index 0. The stack2 starts from the rightmost corner, the first element in stack2 is pushed at index (n-1).

Both stacks grow (or shrink) in opposite direction.

To check for overflow, all we need to check is for space between top elements of both stacks. This check is highlighted in the below code.
'''

# top1, top2  .    记录顶部就可以   反方向

# space efficient