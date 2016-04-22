# encoding=utf-8
'''
Given a sorted array of integers, write a function that will return the number with the biggest number of repetitions.
'''
#有点像geeks。 但是geeks是 0~k-1的范围。 然后不是sorted。 这个是sorted

#想太多了。 应当没有log的解法.  下面这个O(n), O(1)的才是最优解

class Solution:
    def find(self, arr):
        if not arr: raise ValueError
        ret = (1, arr[0]); cnt=1; i=0
        while i<len(arr):
            cnt = 1
            while i+1<len(arr) and arr[i+1]==arr[i]:
                i+=1; cnt+=1
            ret = max(ret, (cnt, arr[i]))
            i+=1
        return ret
'''
class Solution:
    def find(self, arr):
        if not arr: raise ValueError
        ret = (1, arr[0]); cnt=1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:  cnt+=1
            else:
                ret = max(ret, (cnt, arr[i-1]))
                cnt=1
        return ret
'''
s = Solution()
print s.find([1, 1, 2, 3])
print s.find([1, 1, 2, 2, 3, 3, 3, 4])


#想到一个解法是klogN的。   k是unique number数量。  就是每个元素cnt的时候用binary search。 然后重新设置。 当unique number很少的时候， N很大的时候比较优秀。

# 比如地球上的人。 找某个年龄的人最多。