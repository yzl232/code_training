# encoding=utf-8
'''
/**
* Implement a function OneEditApart with the following signature:
* bool OneEditApart(string s1, string s2)
*
* OneEditApart("cat", "dog") = false
* OneEditApart("cat", "cats") = true
* OneEditApart("cat", "cut") = true
* OneEditApart("cat", "cast") = true
* OneEditApart("cat", "at") = true
* OneEditApart("cat", "acts") = false
* Edit is: insertion, removal, replacement
*/
'''
#总共就差1和长度相等2种情况。  长度相等很好解决。  差一也好解决。
class Solution:
    def oneEdit(self, a, b):
        small = a;  big = b
        if len(small)>len(big):   small, big = big, small
        operations = 0
        if len(big) - len(small)>1: return False
        elif len(big) == len(small): #长度相等。
            for i in range(len(small)):
                if big[i] != small[i]:
                    if operations >0: return False
                    operations+=1
        else:  #长度不等
            for i in range(len(small)):
                if small[i] != big[i+operations]:
                    if operations >0: return False
                    operations+=1

#
'''



        else:
            for i in range(len(big)):
                if big[i] == small[i]: continue
                else:
                    if small == big[:i]+big[i+1:]: return True
                    return False
'''