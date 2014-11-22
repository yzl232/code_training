# encoding=utf-8
'''
3Sum 变体，每个数字可以重复用。

用pointer的话，是这样子的。。。。

 left =i+1改成 left=i

 left <= right


我觉得可以转化为3 sum problem.   因为3个数。 每个数最多重复3次。
        num = list(set(num))
        num = num+num+num
        num.sort()

用hash也可以。  N2可以存所有2元的sum

'''
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num = list(set(num))
        num = num+num+num
        num.sort()
        res = set()
        for i in range(len(num)-2):
            if i>0 and num[i] == num[i-1]: continue
            left = i #改了这里
            right = len(num)-1; target = 0 - num[i]
            while left <= right:  #改了这里
                if num[left] + num[right] == target:
                    res.add((num[i], num[left], num[right]))
                    left+=1; right -=1
                elif num[left] + num[right] < target:
                    left+=1
                else:
                    right -=1
        return [list(i) for i in res]




'''
以下是leetcode原题
'''
class Solution2:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num = list(set(num))
        num = num+num+num  #这样也是可以的。
        num.sort()
        res = set()
        for i in range(len(num)-2):
            if i>0 and num[i] == num[i-1]: continue
            left = i+1; right = len(num)-1; target = 0 - num[i]
            while left < right:
                if num[left] + num[right] == target:
                    res.add((num[i], num[left], num[right]))
                    left+=1; right -=1
                elif num[left] + num[right] < target:
                    left+=1
                else:
                    right -=1
        return [list(i) for i in res]
s = Solution()
print s.threeSum([-1, 2, 5, 0, 6, -3])
