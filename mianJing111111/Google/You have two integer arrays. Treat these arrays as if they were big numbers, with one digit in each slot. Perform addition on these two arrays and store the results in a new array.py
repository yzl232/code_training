# encoding=utf-8
'''
You have two integer arrays. Treat these arrays as if they were big numbers, with one digit in each slot. Perform addition on these two arrays and store the results in a new array
'''
class Solution:
    def addArrays(self, a, b):
        n = max(len(a), len(b))
        c = [0 for i in range(n)]
        i=len(a)-1; j=len(b)-1; carry=0
        for k in range(n-1, -1, -1):
            s = carry
            if i>=0:
                s+=a[i]
                i-=1
            if j>=0:
                s+=b[j]
                j-=1
            s, carry = s%10, s/10
            c[k]=s
        if carry: return [carry]+c
        return c
s = Solution()
print s.addArrays([9, 9, 9], [1, 1])
print s.addArrays([2, 3, 4], [9, 9])
