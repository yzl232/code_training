# encoding=utf-8
'''
In 1-9 keypad one key is not working. If some one enters a password then not working key will not be entered. You have given expected password and entered password. Check that entered password is valid or not
Ex: entered 164, expected 18684 (you need to take care as when u enter 18684 and 164 only both will be taken as 164 input)


简单的说就是同时比较。 出现不匹配，
比较faultkey。 第一次就置为faultkey,
如果与faultkey相等。 继续匹配。 否则return False


'''

class Solution:
    def isMatch(self, actual, expected, faultKey = ''):
        i=j=0
        while i<len(actual) and j<len(expected):
            if actual[i] != expected[j]:
                if faultKey=='': faultKey=expected[j]
                elif faultKey!=expected[j]: return False
            else:  i+=1
            j+=1
        while j<len(expected) and expected[j] ==faultKey: j+=1
        return i==len(actual) and j==len(expected)

s = Solution()
print s.isMatch('164', '186848')
print s.isMatch('164', '186847')