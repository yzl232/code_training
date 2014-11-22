# encoding=utf-8
'''

Given an array of integers. We have to find the max element of the array, which is at multiple places in the array and return any one of the indices randomly.


简单做法1：
1. Go through the array once, find the max and the number of occurrences (n).
2. Generate a random number (r) between 1 and n.
3. Go through the array again, return rth occurrence.

Time: O(n)
Space: O(1)


two  pass


做法2：

to complete this solution ,
start with 3 variable
1) currentMaxNum = current max number
2) currentMaxCount = how many instances of current max we have seen

every time we update currentMaxNum we update the currentMaxCount to 0.
initialize {currentMaxNum , CurrentMaxCount} ={a[0],1}
foreach a[i]
if (a[i] < currentMaxNum) -- continue;
else if ( a[i] > currentMaxNum)
{
currentMaxNum = a[i]; currentMaxCount = 0;
}
else
{
// a[i] == currentMaxNum
currentMaxCount ++;
replace currentMaxNum with a[i] with probability 1 / currentMaxCount;
}

This algorithm guarantees that currentMaxNum will be max number at the end.
now lets say there are 5 max in the array all over the array .
the first element will get selected with 100% (first time). the chances that it will remain the final outout that it has to survive the next 4 coin toss. which means
1* (1 -1/2) * (1-1/3)*(1-1/4)*(1-1/5) = 1*1/2/*2/3*3/4*4/5 = 1/5

prob that 2nd max becomes the final number =
(1/2)*(1-1/3)*(1-1/4)*(1-1/5) = 1/5. ....

though my first thought was to simply count the total number of max element in first pass and just generate a random number (x) between 1 to 5 ( if 5 is the total count) and in 2nd pass simply return the xth element.



又一个不错的想法
Worst case space complexity could be O(N) - if all the elements are max values (cause you store max elements in a separate list/array).

If we can modify array - better in terms of space complexity:
1. Do in-place random shuffle of array.
2. Choose only one max element.

time: O(N)
space: O(1)
'''

#这个做法是最优解。
import random

def rand_max(arr):
	curr_max = 0
	curr_max_idx = 0
	curr_max_count = 1
	for i,x in enumerate(arr):
		if x > curr_max:
			curr_max = x
			curr_max_idx = i
			curr_max_count = 1
		elif x == curr_max:
			curr_max_count = curr_max_count + 1
			if random.random() < 1.0 / curr_max_count:   #replace currentMaxNum with a[i] with probability 1 / currentMaxCount;
				curr_max_idx = i
	return curr_max_idx