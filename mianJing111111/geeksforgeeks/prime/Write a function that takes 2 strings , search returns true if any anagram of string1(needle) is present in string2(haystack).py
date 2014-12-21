# encoding=utf-8
'''
// cat, actor -> T
// car, actor -> F

bool anaStrStr (string needle, string haystack)
{
}

Write a function that takes 2 strings , search returns true if any anagram of string1(needle) is present in string2(haystack)


我想到的解法。是建立一个hashMap . 然后把所有的permutation 存进去。 O(n!)+O(m)

用素数是更好的方法:  O(m)


把每个ch。 hash。 然后求和。
'''
#用sliding window 应当是期待的解法 O(n )


'''
Given two strings a and b, find whether any anagram of string a is a sub-string of string b. For eg:
if a = xyz and b = afdgzyxksldfm then the program should return true.
'''

#prime也是很妙的想法。 但是应当不是主流。 主流是sliding window

#facebook也有考过

#看来是google的高频的题目


#anagram.  这是与strstr不同的地方
#G家的题目吧

#和leetcode minimum windows substring基本一样。 区别只在于 当length相等时，返回true

pass



class Solution:
    # @return a string
    def minWindow(self, s, t):
        ls = len(s); lt = len(t); ret = ''
        if ls<lt: return ''  #到达了长度，就一直尝试缩减窗口
        st = 0;    #关键是用了2个hashtable。 另外缩减窗口。
        fdN = 0; tcnt ={}; fnd = {}
        for ch in t:
            if ch not in tcnt: tcnt[ch]=0
            tcnt[ch]+=1
        for end in range(ls):
            ch = s[end]
            if ch not in tcnt: continue
            if ch not in fnd or tcnt[ch] > fnd[ch]: fdN+=1    #fndC之后不会再动了
            if ch not in fnd:  fnd[ch]=0
            fnd[ch]+=1    #这两行照抄上面tcnt部分的
            if fdN == lt:  #has
                while s[st] not in tcnt or fnd[s[st]] > tcnt[s[st]]:
                    if s[st] in t: fnd[s[st]] -=1
                    st +=1
                if len(t)==end-st+1: return True
        return False
#O(n)
s = Solution()
print s.minWindow('actor', 'cat')
print s.minWindow('afdgzyxksldfm', 'xyz')
print s.minWindow('actor', 'car')


'''
class Solution:
    def isprime(n):
        if n<=1: return False
        if n==2 or n==3: return True
        if n%2==0:     return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:    return False
        return True

    def prime26(self):
        arr = [2, 3, 5, 7]
        for i in range(11, 1000):
            if len(arr)>=26: break
            if self.isprime(i): arr.append(i)
        return arr

    def anaStrStr(self, s1, s2):
        n = len(s1) ;  m=len(s2)
        arr =self.prime26()
        d = {chr(ord('a')+i):arr[i] for i in range(26) }
        product = self.product(s1, d)
        if n>m: return False
        for i in range(m-n):
            tmp = s2[i:i+n]
            if self.product(tmp, d)==product: return True
        return False

    def product(self, s, d):
        ret = 1
        for ch in s:
            ret*=d[ch]
        return ret
'''