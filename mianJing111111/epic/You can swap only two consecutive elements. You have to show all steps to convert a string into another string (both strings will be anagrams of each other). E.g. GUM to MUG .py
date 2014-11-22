# encoding=utf-8
'''
You can swap only two consecutive elements. You have to show all steps to convert a string into another string (both strings will be anagrams of each other). E.g. GUM to MUG

GUM
GMU
MGU
MUG


很像插入排序啊。 我研究一下。

while每次都检查一下i+1,  j-1

'''

class Solution:
    def transition(self, a, b):
        if len(a)!= len(b): return
        n = len(a);  i=j=0
        a = list(a); b = list(b)
        while i<n:
            j = i
            while a[j] != b[i]:  #找到目标char
                j+=1
            while j>i:
                a[j-1], a[j] = a[j], a[j-1]  #逐个往前挪。swap  a[j], a[j-1]
                print ''.join(a)
                j-=1
            i+=1

s = Solution()
s.transition("ACADBB123", "DC1BA32BA")
