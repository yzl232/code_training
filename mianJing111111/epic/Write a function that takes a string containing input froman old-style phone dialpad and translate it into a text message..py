# encoding=utf-8
'''

Write a function that takes a string containing input from an old-style phone dial pad and translate it into a text message.

Enter a key multiple times in a row prints the next character in the sequence, so “2”=”A”, “22”=”B”, “222”=”C”, “2222”=”2”. This sequence wraps, so “22222”=”A”, “#” signals the start of a new character:“2#22”=”AB”.

'''
#也是使用prev指针， 跟新数cnt这种思路. 灵位最后多更新一句
class Solution:
    def text(self, s):
        if not s: return ''
        d = {0:[''], 1:[''], 2:['a', 'b', 'c', '2'], 3:['d', 'e', 'f', '3']}
        prev = s[0]; count=1
        result = ''
        for i in range(1, len(s)):
            ch = s[i]
            if ch==prev: count+=1
            else:
                if prev!='0' and prev!='1' and prev!='#':   result+=d[int(prev)][(count-1)%4]
                count=1
                prev = ch
        if prev!='0' and prev!='1' and prev!='#':   result+=d[int(prev)][(count-1)%4]
        return result
s = Solution()
print s.text("222#22323#3")