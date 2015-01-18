# encoding=utf-8
'''
Convert string into new string e.g. "abcD"->"cdeF" and "plxY" -> "rnzA"
'''
class Solution:
    def convert(self, s, shift = 2):
        ret = ''
        for ch in s:  # 'a' =>97.      'A'=>65  记忆。 都是16的倍数+1
            if 'a'<=ch<='z':  ret+=chr((ord(ch)-97+shift)%26+97)    #%26= 0~25,  加上'a'正好
            if 'A'<=ch<='Z': ret+=chr((ord(ch)-65+shift)%26+65)
        return ret

s = Solution()
print s.convert('abcD')