# encoding=utf-8
'''
You can swap only two consecutive elements.
Show all steps to convert a string into another string (both strings will be anagrams of each other). E.g. GUM to MUG

GUM
GMU
MGU
MUG


很像插入排序啊。 我研究一下。

while每次都检查一下i+1,  j-1

'''

class Solution:
    def transition(self, a, b):
        assert sorted(a)==sorted(b)
        n = len(a);  j=0
        a = list(a); b = list(b)
        while j<n:
            i = j
            while a[i] != b[j]:  i+=1 ##找到目标char
            while i>j:
                a[i-1], a[i] = a[i], a[i-1]  #逐个往前挪。swap  a[i], a[i-1]
                print ''.join(a)
                i-=1
            j+=1

s = Solution()
s.transition("ACADBB123", "DC1BA32BA")
