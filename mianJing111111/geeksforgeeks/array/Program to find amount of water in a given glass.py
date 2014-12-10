# encoding=utf-8
'''
Program to find amount of water in a given glass

There are some glasses with equal capacity as 1 litre. The glasses are kept as follows:

    			   1
		         2   3
		      4    5    6
		    7    8    9   10

You can put water to only top glass. If you put more than 1 litre water to 1st glass, water overflows and fills equally in both 2nd and 3rd glasses. Glass 5 will get water from both 2nd glass and 3rd glass and so on.
If you have X litre of water and you put that water in top glass, how much water will be contained by jth glass in ith row?

Example. If you will put 2 litre on top.
1st – 1 litre
2nd – 1/2 litre
3rd – 1/2 litre


The approach is similar to Method 2 of the Pascal’s Triangle. If we take a closer look at the problem, the problem boils down to Pascal’s Triangle.

                           1   ---------------- 1
		                 2   3 ---------------- 2
                       4    5    6  ------------ 3
		             7    8    9   10  --------- 4

Each glass contributes to the two glasses down the glass. Initially, we put all water in first glass. Then we keep 1 litre (or less than 1 litre) in it, and move rest of the water to two glasses down to it. We follow the same process for the two glasses and all other glasses till ith row. There will be i*(i+1)/2 glasses till ith row.
'''
class Solution:
    def findWater(self, r, c, x):
        if c>r: return
        glass = [0 for k in range((r+1)*r/2)]  #等差数列,
        glass[0] = x; p = 0
        for i in range(r):
            for j in range(c):
                x = glass[p]
                glass[p] = 1 if x>=1 else x
                x = x-1 if x>=1 else 0
                glass[p+i] += x/2
                glass[p+i+1] +=x/2
                p+=1
        return glass[r*(r-1)/2+c-1]  #因为从0开始。所以最后减一