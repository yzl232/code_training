# encoding=utf-8
'''
You are given a string which has numbers and letters. Numbers occupy all odd positions and letters even positions. You need to transform this string such that all letters move to front of array, and all numbers at the end.

The relative order of the letters and numbers needs to be preserved

I need to do this in O(n) time and O(1) space.

eg: a1b2c3d4 -> abcd1234 , x3y4z6 -> xyz346

Please don't submit your answers if it is not fulfilling the time-space complexity requirements.
'''

'''
The characters in odd positions must be moved to the last half and that's what the solution shown in geeksforgeeks does. However the problem also states that those characters are digits. This is not required for the geeksforgeeks solution to work but using this fact allows a much simpler solution (this one here).
'''






class Solution:
    def transForm(self, s):
        end = len(s); begin=0
        m = end/2; cnt=0
        for i in range(1, m):
            if '0'<= s[i]<='9':
                j = i
                j=j/2+j%2*m
                while j!=i:
                    print s, i, j
                    s[i], s[j] = s[j], s[i]
                    j=j/2+j%2*m
                    cnt+=1
        return s, cnt
s = Solution()
print s.transForm(list('a1b2c3d4'))
print s.transForm(list('x3y4z6'))
