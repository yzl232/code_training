# encoding=utf-8
'''
Given an array write a function to print all continuous subsequences in the array which sum of 0.
e.g:
Input:
Array = [-1, -3, 4, 5, 4]
output:
-1, -3, 4

暴力法。 寻找所有start, end。  O(n2)

O(n)



1) run cumulate sum on the original array
2) append [0] in font of this cum_sum_array
3) check if two item in this cum_sum_array are same (for requirement sum==0, this could be done in O(n))



# 最极端的最坏情况还是 O(n2)
平均来说是O(n)

很巧妙


关于subsequence  如果是说 continuous 关于subsequence。 那就是正常的subarray。 否则就是按顺序的subsequence


之前的和，也就是左边的和
'''

'''
1) 给个数组seq， 和一个total，找 if there is a contiguous sequence in seq
which sums to total.

也是facebook面经的变体。

geeks也有这道题目
'''

class Solution:
    def print0S(self, arr):  #非常好的代码。    cumulative sum
        d = {0: [-1]}
        s = 0
        for i in range(len(arr)):
            s+=arr[i]
            if s in d:
                for start in d[s]:   print arr[start+1:i+1]  #稍作修改
                d[s].append(i)
            else:  d[s] = [i]      #key是cumulative sum, value index
s = Solution()
print s.print0S([-1, -3, 4, 5, 4, -2, -2, 0,  4])