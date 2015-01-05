# encoding=utf-8
'''
一个数组，大小(1M+1)，包含了所有1到1M（M表示一百万）的整数，因此，必有一
个数重复，请找出这个数。尽量说所有可能的解法
'''
'''
一百万不算大。  可以视作普通的N
`1  hashtable
2   求和。 然后减掉 （1+1m）*(1m)/2
3
方法2： Use array elements as index
在  Check if array elements are consecutive  也有出现

不适合负数。 适合发现repeat  。  而且可以发现任何repeat
#leetcode是find first missing positive  也就是说，找missing 。 没范围。 有负数
'''
class Solution:
    def findRep(self, arr):
        for i in range(len(arr)):
            tmp = abs(arr[i])  #就是利用负号。 增加了信息
            if arr[tmp]>0:  arr[tmp] = -arr[tmp]
            else:  print tmp
