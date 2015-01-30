# encoding=utf-8
# 2 sum closest
#类似leetcode 3sum closest
class Solution3:
    def twoSum(self, num):
        num.sort()
        i=0;  j=len(num)-1; ret=(None, None, 10**10)
        while i<j:
            cur = num[i]+num[j]
            diff = abs(0-cur)
            if diff<ret[-1]: ret = (num[i], num[j], diff)
            if cur == 0: return num[i], num[j]
            elif cur > 0:  j-=1
            else: i+=1
        return ret