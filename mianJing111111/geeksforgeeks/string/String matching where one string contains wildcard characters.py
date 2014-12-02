# encoding=utf-8
'''

String matching where one string contains wildcard characters

Given two strings where first string may contain wild card characters and second string is a normal string. Write a function that returns true if the two strings match. The following are allowed wild card characters in first string.

* --> Matches with 0 or more instances of any character or set of characters.
? --> Matches with any one character.

For example, “g*ks” matches with “geeks” match. And string “ge?ks*” matches with “geeksforgeeks” (note ‘*’ at the end of first string). But “g*k” doesn’t match with “gee” as character ‘k’ is not present in second string.


似乎是regular expression matching leetcode

leetcode wildmatch  就是原题

可以直接上最优解。 吓死它


'''