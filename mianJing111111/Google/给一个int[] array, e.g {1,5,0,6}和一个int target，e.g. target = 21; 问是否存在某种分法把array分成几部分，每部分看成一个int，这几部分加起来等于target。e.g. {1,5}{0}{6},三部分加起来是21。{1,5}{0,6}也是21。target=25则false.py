# encoding=utf-8
'''
第二题是给一个int[] array, e.g {1,5,0,6}和一个int target，e.g. target = 21;
问是否存在某种分法把array分成几部分，每部分看成一个int，这几部分加起来等于target。e.g. {1,5}{0}{6},三部分加起来是21。{1,5}{0,6}也是21。target=25则false
'''
#应当意思是Input是string
# encoding=utf-8
'''
Given a string of digits, find the minimum number of additions required for the string to equal some target number. Each addition is the equivalent of inserting a plus sign somewhere into the string of digits. After all plus signs are inserted, evaluate the sum as usual. For example, consider the string "12" (quotes for clarity). With zero additions, we can achieve the number 12. If we insert one plus sign into the string, we get "1+2", which evaluates to 3. So, in that case, given "12", a minimum of 1 addition is required to get the number 3.
'''
#没想到好办法。 暴力吧。
#
class Solution:
    def solve(self, s, target):
        n = len(s)-1;   ret = n+10
        for i in range(2**n):
            cur = 0;  x=0; cnt=0
            for j in range(n+1):
                cur = cur*10+int(s[j])
                if (1<<j) & i:   #1<<j作用是， 在第k位设置一个set bit
                    x+=cur
                    cnt+=1
                    cur=0
            x+=cur
            if x==target:  ret = min(ret, cnt)
        if ret==n+10:  return -1
        return ret
s = Solution()
print s.solve('12', 3)