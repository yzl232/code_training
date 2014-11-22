# encoding=utf-8
'''
There are a large number of leaves eaten by caterpillars. There are 'K"' caterpillars which jump onto the leaves in a pre-determined sequence. All caterpillars start at position 0 and jump onto the leaves at positions 1,2,3...,N. Note that there is no leaf at position 0.
Each caterpillar has an associated 'jump-number'. Let the jump-number of the i-th caterpillar be A [i]. A caterpillar with jump number 7 keeps eating leaves in the order 1,241,3*1,... till it reaches the end of the leaves - i.e, it eats the leaves at the positions which are multiples of /'.
Given a set 'A' of 'IC elements. 'e<=15.,. 'N'<=109, we need to determine the number of uneaten leaves.
Input Format:
N -number of leaves
A - Given array of integers
Output Format:
An integer denoting the number of uneaten leaves.
Sample Input:
N = 10.     (1~10)
A = [2,4,5]
Sample Output:
4
Explanation
1,3,7,9 are the leaves which are never eaten. All leaves which are multiples of 2, 4, and 5 have been eaten.

 题目太长懒得看。 直接看input, output


 #hashtable 可以秒杀40%的题目！！！！！！
'''
class Solution:
    def countUneaten(self, n, arr):
        uneaten = 0
        eaten = 0
        positionEatenHash = {}
        for i in arr:
            for j in range(1, n/i+1):
                if i*j not in positionEatenHash:
                    positionEatenHash[i*j] = 1
        print positionEatenHash
        return n-len(positionEatenHash)

s = Solution()
print s.countUneaten(10, [2, 4, 5])

