# encoding=utf-8
'''
Convert string into new string e.g. "abcD"->"cdeF" and "plxY" -> "rnzA"
'''

class Solution:
    def convert(self, s, shift = 2):
        result = ''
        for ch in s:
            if 'a'<=ch<='z':  result+=chr((ord(ch)-ord('a')+shift)%26+ord('a'))
            if 'A'<=ch<='Z': result+=chr((ord(ch)-ord('A')+shift)%26+ord('A'))
        return result

