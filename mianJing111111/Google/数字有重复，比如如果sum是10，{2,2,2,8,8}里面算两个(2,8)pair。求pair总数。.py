# encoding=utf-8
'''
数字有重复，比如如果sum是10，{2,2,2,8,8}里面算两个(2,8)pair。求pair总数。
'''
#还是hashtable和2 pointer两种

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}; cnt=0
        for x in num:
            if x not in d: d[x]=0
            d[x]+=1
        for x in d:
            if target-x in d:  
                if x==target-x: cnt+=d[x]/2
                else: cnt+=min(d[x], d[target-x])  #{2,2,2,8,8}里面算两个(2,8)pair
        return cnt/2
s = Solution()
print s.twoSum([2, 2, 2, 8, 8], 10)



#假如是sorted , 那么用two  pointer可以做到O(1) space

class Solution3:
    def twoSum(self, num, target):
        i=0;  j=len(num)-1; cnt=0
        while i<j:
            cur = num[i]+num[j]
            if cur == target:
                cnt+=1
                i+=1;  j-=1          #{2,2,2,8,8}里面算两个(2,8)pair.  所以同时i+1, j-1
            elif cur > target:  j-=1
            else: i+=1
        return cnt
s = Solution3()
print s.twoSum([2, 2, 2, 8, 8], 10)
