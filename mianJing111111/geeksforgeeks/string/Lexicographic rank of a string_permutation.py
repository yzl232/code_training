# encoding=utf-8
'''

Lexicographic rank of a string

Given a string, find its rank among all its permutations sorted lexicographically. For example, rank of “abc” is 1, rank of “acb” is 2, and rank of “cba” is 6.

For simplicity, let us assume that the string does not contain any duplicated characters.

One simple solution is to initialize rank as 1, generate all permutations in lexicographic order. After generating a permutation, check if the generated permutation is same as given string, if same, then return rank, if not, then increment the rank by 1. The time complexity of this solution will be exponential in worst case. Following is an efficient solution.

Let the given string be “STRING”. In the input string, ‘S’ is the first character. There are total 6 characters and 4 of them are smaller than ‘S’. So there can be 4 * 5! smaller strings where first character is smaller than ‘S’, like following

R X X X X X
I X X X X X
N X X X X X
G X X X X X

Now let us Fix S’ and find the smaller strings staring with ‘S’.

Repeat the same process for T, rank is 4*5! + 4*4! +…

Now fix T and repeat the same process for R, rank is 4*5! + 4*4! + 3*3! +…

Now fix R and repeat the same process for I, rank is 4*5! + 4*4! + 3*3! + 1*2! +…

Now fix I and repeat the same process for N, rank is 4*5! + 4*4! + 3*3! + 1*2! + 1*1! +…

Now fix N and repeat the same process for G, rank is 4*5! + 4*4 + 3*3! + 1*2! + 1*1! + 0*0!

Rank = 4*5! + 4*4! + 3*3! + 1*2! + 1*1! + 0*0! = 597

Since the value of rank starts from 1, the final rank = 1 + 597 = 598


这道题目就是leetcode  permutation sequence的变体.
就是反过来而已
'''
import math
class Solution:
    def countSmallerRight(self, arr, l):
        return sum(1  for i in range(l+1, len(arr)) if arr[i]<arr[l])

    def findRank(self, arr):
        n = len(arr)
        m = math.factorial(n)
        rank = 0
        for i in range(len(arr)):
            m/= n-i     #n, n-1, n-2, ...
            rank+=m*(self.countSmallerRight(arr, i))        #在它前面的有多少个。
        return rank+1
s = Solution()
print s.findRank(['c', 'b', 'a'])
'''
N2


The above programs don’t work for duplicate characters. To make them work for duplicate characters, find all the characters that are smaller (include equal this time also), do the same as above but, this time divide the rank so formed by p! where p is the count of occurrences of the repeating character.


    def findRank(self, arr):
        n = len(arr)
        m = self.fact(n)
        rank = 0
        for i in range(len(arr)):
            m/= n/i
            cnt = self.countSmallerOrEqualRight(arr, i)
            rank+=cnt*m
        return rank/()


      abb      bab   bba    6/2!    （因为bb 种类是2！）
    aabb     24/(2!)/(2!)     （因为aa,  bb 种类是 2！ * 2！）


'''