# encoding=utf-8
'''
Asked by SG
Given an array in which all numbers except two are repeated once. (i.e. we have 2n+2 numbers and n numbers are occurring twice and remaining two have occurred once). Find those two numbers in the most efficient way.


第一想法用hash。 用 extra space. but efficient

XOR of two different numbers x and y results in a number which contains set bits at the places where x and y differ. So if x and y are 10...0100 and 11...1001, then result would be 01...1101.

So the idea is to XOR all the elements in set. In the result xor, all repeating elements would nullify each other. The result would contain the set bits where two non-repeating elements differ.

Now, if we take any set bit of the result xor and again do XOR of the subset where that particular bit is set, we get the one non-repeating element. And for other non-repeating element we can take the subset where that particular bit is not set.

We have chosen the rightmost set bit of the xor as it is easy to find out.


第一道题，是说你知道(n&(n-1))得出什么结果吗？
  “n&(n-1)”改变最后一位digit 是1得


举个例子就好。 3&(3-1)

'''

class Solution:
    def get2NonRepeatingNos(self, arr):
        xor = 0
        for i in arr:
            xor ^= i
        bit = xor & ~(xor-1)  #Get the rightmost set bit in    set_bit_no
        x = y =0
        for i in arr:
            if bit & i:
                x ^=i
            else:
                y ^=i
        return x, y

s = Solution()
print s.get2NonRepeatingNos([2, 3, 7, 9, 11, 2, 3, 11])
#和这道题目重复： Find the two numbers with odd occurrences in an unsorted array