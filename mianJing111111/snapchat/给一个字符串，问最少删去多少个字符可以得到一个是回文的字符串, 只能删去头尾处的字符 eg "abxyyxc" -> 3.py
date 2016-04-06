#给一个字符串，问最少删去多少个字符可以得到一个是回文的字符串, 只能删去头尾处的字符 eg "abxyyxc" -> 3

#G家有类似的。给一个STR，删除最少的任何char,使它变成palindrome.
# 求str和翻转str的longest common subsequence，然后剩下的部分就是必须要删的
# 只删除头尾的话， 就是longest common substring.   
'''
http://www.1point3acres.com/bbs/thread-140489-1-1.html
G家
string题，第一问和leetcode上的shortest palindrome 基本一样，换成了插在结尾，问题不大，讨论了下时间复杂度。
follow up问如果插字符在任何地方，看到过dp解法，但是想不起来也没推出来。搜了一下，类似 pku1159
'''