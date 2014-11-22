# encoding=utf-8
'''
From a given string, replace all instances of 'a' with 'one' and 'A' with 'ONE'.

Example Input:
" A boy is playing in a garden"

Example Output:
" ONE boy is playing in one garden"


-- Not that 'A' and 'a' are to be replaced only when they are single characters, not as part of another word.
'''

class Solution:
    def replaceAa(self, s):
        arr = s.split(" ")
        for i in range(len(arr)):
            if arr[i] == 'a':  arr[i] = 'one'
            elif arr[i] =='A': arr[i] = 'ONE'
        return ' '.join(arr)
s = Solution()
print s.replaceAa(" A boy is playing in a garden" )