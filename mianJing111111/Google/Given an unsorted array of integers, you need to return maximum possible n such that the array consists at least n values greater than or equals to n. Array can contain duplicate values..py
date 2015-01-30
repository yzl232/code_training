# encoding=utf-8
'''
Given an unsorted array of integers, you need to return maximum possible n such that the array consists at least n values greater than or equals to n. Array can contain duplicate values.
Sample input : [1, 2, 3, 4] -- output : 2
Sample input : [900, 2, 901, 3, 1000] -- output: 3
'''

#看过2次了

'''
Lets say the array has M numbers. For the purpose of this problem, negative values and 0s are irrelevant. Also, numbers larger than M can be treated as M because the answer is never larger than M.

So, we can count the number of existing values between 1 and M. Then, process the values backwards (M to 1) to find the answer, adding the counts of the values processed so far.

'''

class Solution: #和原本array没太大关系 我们建立0~N的cnt  array。 因为结果可能是0~N。
    def solve(self, vals):  #返回的n是数目， 实际上处于0~n之间。  这样子要大于等于n。 我们忽略负数.
        n = len(vals); curN=0
        cnt = [0]*(n+1) #cnt[i] cnt数目。
        for x in vals:
            if x>=n:  cnt[n]+=1   #大于等于n的视为n
            elif x>=0: cnt[x]+=1   # ignore negative values
        for i in range(len(cnt)-1, -1, -1):   # 0~n  为了对应cnt array
            curN +=cnt[i]  #非常巧妙
            if curN>=i:  return i
        return 0


s = Solution()
print s.solve([900, 2, 901, 3, 1000])