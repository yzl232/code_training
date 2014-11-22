# encoding=utf-8
'''
Given a number, can you remove k digits from the number so that the new formatted number is smallest possible.
input: n = 1432219, k = 3
output: 1219

7459282641      k=3     4282641
7451982641      k=3     1982641


7459282641      k=3
第一步：  在前k+1位中。 找到第一个最小的数。  移除掉之前的数。
第二步：  4+ 59282641 .    还可以移除2个数。 前三个数找最小的。 移除前面的。
     4+282641

In the leftmost k+1 digits, find the largest one (let us say it is located at ith location. In case there are multiple occurrences choose the leftmost one). Keep it. Repeat the algorithm for k_new = k-i+1, newNumber = i+1 to n digits of the original number.



更好的方法。

两个两个比较。  每次删掉一个。 直到删除满了。
每次比较arr[0]  和  arr[1]

先从左到右，如果左边的digit比右边的大，就删除左边的digit，如果删
除不够k个digit则把最后的几位删掉，

'''
class Solution:
    def removeK(self, n, k):
        arr = list(str(n))
        length = len(arr)
        while k>0:
            small = 0
            if arr[0]>arr[1]:  small = 1
            arr = [arr[small]] + arr[2:]
            k = k - 1  #已经删除了几个
        return ''.join(arr)

s = Solution()
print s.removeK(1432219, 2)
print s.removeK(1432219, 3)
print s.removeK(1432219, 4)
print s.removeK(7454982641, 3)
print s.removeK(7459282641, 3)
print s.removeK(7451982641, 3)
print s.removeK(7459282641, 4)