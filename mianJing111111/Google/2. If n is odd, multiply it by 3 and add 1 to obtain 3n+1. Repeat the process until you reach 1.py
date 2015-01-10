# encoding=utf-8
'''
题目：Do you know the Collatz conjecture? (Yes, I do  lz学math的) Given an integer n. If n is even, divide it by 2 to get n/2. If n is odd, multiply it by 3 and add 1 to obtain 3n+1. Repeat the process until you reach 1. Count the numbers visited through this process and denote it by cycle(n). Write a function that takes in two integers i,j (i < j), return max(cycle(k)), for i <= k <= j.
'''

def collatz_sequence(x):
    cnt = 0
    while x > 1:
       if x % 2 == 0:  x = x / 2
       else:  x = 3 * x + 1
       cnt+=1    # Added line
    return cnt

def findBig(i, j):
    return max(collatz_sequence(x) for x in range(i, j+1))