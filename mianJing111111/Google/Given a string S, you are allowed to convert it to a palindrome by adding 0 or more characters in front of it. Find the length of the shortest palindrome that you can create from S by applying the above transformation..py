# encoding=utf-8
'''
Given a string S, you are allowed to convert it to a palindrome by adding 0 or more characters in front of it.
Find the length of the shortest palindrome that you can create from S by applying the above transformation.
'''

#和以前不大一样。 以前是任意位置插入都算。

#  the time complexity gets reduced by simply finding palindrome that start from first character.

# O(n)   in place
# find longest palindrome prefix
#  KMP 可以做O(n)


'''
The thing is, the time complexity gets reduced by simply finding palindrome that start from first character. If we reduce the suffix tree implementation:

1. Create suffix tree from the reverse string (Ukkonen proved this is O(n))
2. Walk this tree from the beginning with the original string until there is path.

This is largest palindrome that starts with beginning. So you need to add [original string length] - [found polyndrome] characters in the front
'''