# encoding=utf-8
'''
 In an unsorted array of numbers that occurs an odd number of times except one that occurs an even number of times, find the number that occurs an even number of times
'''

#做法1. 用hashmap统计了。  最后找出唯一一个frequency为偶数次

# hashmap最好







#做法2. set记录unique的数目。  xor一遍后， 剩下的是所有奇数的xor。 再xor所有的unique的key

#两种做法复杂度相同。
#总就是要O(n) space



'''
class Solution:
    def xxx(self, arr):
        ret = 0; unique=set([])
        for x in arr:
            ret^=x
            unique.add(x)
        for x in unique:
            ret^=x
        return ret

s = Solution()
print s.xxx([1,4 , 3, 5, 3])
'''