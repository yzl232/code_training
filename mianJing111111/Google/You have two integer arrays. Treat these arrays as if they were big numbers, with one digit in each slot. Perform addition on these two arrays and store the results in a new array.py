# encoding=utf-8
'''
You have two integer arrays. Treat these arrays as if they were big numbers, with one digit in each slot. Perform addition on these two arrays and store the results in a new array
'''
class Solution:
    def addArrays(self, a, b):
        m, n =len(a), len(b)
        x=max(m, n); carry=0;  ret=[None]*x
        for i in range(-1, -x-1, -1):
            s = carry+(0 if i<-m else a[i])+(0 if i<-n else b[i])
            s, carry = s%10, s/10
            ret[i]=s
        return ret if not carry else [carry]+ret
s = Solution()
print s.addArrays([9, 9, 9], [1, 1])
print s.addArrays([2, 3, 4], [9, 9])


#因为觉得三个指针太麻烦。 一个足够
'''
class Solution:
    def addArrays(self, a, b):
        n = max(len(a), len(b))
        c = [0]*n;  carry=0
        i=len(a)-1; j=len(b)-1        #用到三个指针。
        for k in range(n-1, -1, -1):
            s = carry
            if i>=0:     s+=a[i]
            if j>=0:     s+=b[j]
            i-=1; j-=1
            s, carry = s%10, s/10
            c[k]=s
        if carry: return [carry]+c
        return c
s = Solution()
print s.addArrays([9, 9, 9], [1, 1])
print s.addArrays([2, 3, 4], [9, 9])
'''