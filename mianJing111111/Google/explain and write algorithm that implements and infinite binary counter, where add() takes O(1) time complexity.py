# encoding=utf-8
'''
explain and write algorithm that implements and infinite binary counter, where add() takes O(1) time complexity
'''

'''
we keep an aggregation on consecutive 1 or 0.

meaning 111000111 is <3,1> <3,0> <3,1>

1) if the first bulk is of 1's. it turns to bulk of 0`s and turn the very next 0 to 1.

we now check if we can aggregate bulks of 1's.

2) if the first bulk is of 0's, we make the first digit 1. and see if we can aggregate 1's.
'''