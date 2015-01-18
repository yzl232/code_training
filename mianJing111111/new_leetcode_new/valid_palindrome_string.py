# encoding=utf-8
'''
leetcode简单题目
'''

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i=0; j = len(s)-1; s = s.lower()
        while i<j:
            while i<j and not ('a'<=s[i]<='z' or '0'<=s[i]<='9'): i+=1
            while i<j and not ('a'<=s[j]<='z' or '0'<=s[j]<='9'): j-=1
            if s[i] != s[j]: return False
            i+=1;   j-=1
        return True

'''
上面这个是in-place
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower(); s1 = ''
        for ch in s:
            if 'a'<=ch<='z' or '0'<=ch<='9':s1+=ch
        return s1 == s1[::-1]
'''





'''
public boolean isPalindrome(char[] chars) {
		int start = 0, end = chars.length - 1;
		while (start < end) {
			if (!isLetter(chars[start])) {
				start++;
			} else if (!isLetter(chars[end])) {
				end--;
			} else {
				if (chars[start] == chars[end]
						|| Math.abs(chars[start] - chars[end]) == 'a' - 'A') {
					start++;
					end--;
				} else {
					return false;
				}
			}
		}
		return true;
	}

	private boolean isLetter(char c) {
		return (c > 'a' && c < 'z') || (c > 'A' && c < 'Z');
	}
'''