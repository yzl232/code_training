# encoding=utf-8
'''
Given a string of digits, find the minimum number of additions required for the string to equal some target number. Each addition is the equivalent of inserting a plus sign somewhere into the string of digits. After all plus signs are inserted, evaluate the sum as usual. For example, consider the string "12" (quotes for clarity). With zero additions, we can achieve the number 12. If we insert one plus sign into the string, we get "1+2", which evaluates to 3. So, in that case, given "12", a minimum of 1 addition is required to get the number 3.
'''
#没想到好办法。 暴力吧。

class Solution:
    def solve(self, s, target):  # 2**n  相当于recursion
        self.ret = len(s)+10
        self.dfs(s, target, 0, '')
        return self.ret
    def dfs(self, s, target, cnt, pre):
        if cnt>self.ret or target<0: return
        if not s:
            if target ==0 and not pre:   self.ret = min(self.ret, cnt-1)
            return
        if not s or target<0: return
        self.dfs(s[1:], target, cnt, pre+s[0])  #举例  123.       1+23,  12+3 ,  1+2+3, 123
        self.dfs(s[1:], target-int(pre+s[0]), cnt+1, '')

s = Solution()
print s.solve('12', 3)
print s.solve('123', 6)
'''
class Solution:
    def solve(self, s, target):  # 2**n  相当于recursion
        n = len(s);   ret = n+10
        for i in range(2**(n-1)):
            cur =s= cnt=0
            for j in range(n):
                cur = cur*10+int(s[j])  #1<<j作用是， 在第k位设置一个set bit
                if (1<<j) & i:
                    s+=cur; cnt+=1;  cur=0
            s+=cur  #最后再加一次
            if s==target:  ret = min(ret, cnt)
        if ret==n+10:  return -1
        return ret

s = Solution()
print s.solve('12', 3)
'''