# encoding=utf-8
'''


Remove “b” and “ac” from a given string

Given a string, eliminate all “b” and “ac” in the string, you have to replace them in-place, and you are only allowed to iterate over the string once. (Source Google Interview Question)

Examples:

acbac   ==>  ""
aaac    ==>  aa
ababac  ==>   aa
bbbbd   ==>   d

The two conditions are:
1. Filtering of all ‘b’ and ‘ac’ should be in single pass
2. No extra space allowed.

The approach is to use two index variables i and j. We move forward in string using ‘i’ and add characters using index j except ‘b’ and ‘ac’. The trick here is how to track ‘a’ before ‘c’. An interesting approach is to use a two state machine. The state is maintained to TWO when previous character is ‘a’, otherwise state is ONE.
1) If state is ONE, then do NOT copy the current character to output if one of the following conditions is true
…a) Current character is ‘b’ (We need to remove ‘b’)
…b) Current character is ‘a’ (Next character may be ‘c’)
2) If state is TWO and current character is not ‘c’, we first need to make sure that we copy the previous character ‘a’. Then we check the current character, if current character is not ‘b’ and not ‘a’, then we copy it to output.
'''
class Solution:
    def filterS(self, arr):  #char array
        n = len(arr)
        i=j=0
        while i<n:
            if arr[i]=='b':  i+=1
            elif i+1<=n-1 and arr[i:i+2]=='ac':   i+=2  #有点像decode ways.
            else:
                arr[j] = arr[i]
                j+=1
                i+=1