# encoding=utf-8
'''
Verify if the given password is valid/invalid;
1. must be 5-12 characters long
2. must contain at least one number and one lowercase character
3. a sequence must not be followed by the same sequence (like 123123qs is invalid, 123qs123 is valid)


1)Just count the no of characters and see if it lies between 5 and 12.
2)Keep the count of vowel and number encountered ,it should be greater than 1
3)Create a hash table with substring as key and its end index as value.Before inserting a pair <substring,ending index> in hash table ,check if substring is already present in hashtable, if present then ,its (ending index+1) should not be equal to starting index of this repeated substring.

hashtable 如果已经存在。 start不能等于之前end+1.

这一点很巧妙！

'''
#和leetcode   longest substring有点像

class Solution:
    def valid(self, s):
        if len(s)<5 or len(s)>12: return False
        countlow = 0;  countNum = 0
        for ch in s:
            if 'a'<=ch<='z': countlow+=1
            if '0'<=ch <='9': countNum+=1
        if countlow==0 or countlow==0: return False
        d = {}
        for start in range(0, len(s)):
            sub = ''
            for end in range(start, len(s)):
                sub+=s[end]     #按照这个套路可以降低复杂度
                if sub not in d:d[sub] = (start, end)
                elif sub in d and start == d[sub][-1]+1: return False
        return True
