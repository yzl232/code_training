# encoding=utf-8
'''
given a dictionary of wrods,find the pair of word with following property:
1,the two word don't have same letter.
2,the multiple of the two word's length is maximum.



Find the pair of words in a dictionary that don't no same letter and the product of these two words' length is maximum

N 个字符串, 求无common char的两个字符串的长度的乘积最大.

'''

#G家超级高频的题目
#相当的复杂
'''
Assuming the word is A-Z/a-z only, use a bitmap to set which letters it contains.
e.g. ca => 000....101
bb => 000...010
Iterate over the words。n*n
for each pair of words, AND the bitmaps. Return the first pair that gives a 0 result.

This should be n*k + n*n
'''

# 5 * 5 > 10 * 2

#每次用bitmap  & 取and运算。 为0即可。

'''
http://www.meetqun.com/thread-1838-1-1.html

第一面听起来是个三姐。第一题对于我很难，三姐让我优化了半天我也没给出什么太好的方法，这道题没有code。
题目描述：给了一个dict，里面有很多英文单词（lowercase，only 'a' to 'z'），要求从这个字典中找出两个单词，使得它们之间没有相同的字符，然后它们长度的乘积最大。

，我们可以用一个int（32位）的26位来记录单词中某个字母是否出现过，这样每一个单词对应一个int，比较的时候直接使用&操作可以优化比较的部分，但是仍然需要枚举，复杂度到了O(n^2)，


之后三姐问我能不能继续优化，少比较一些东西，我说每个单词按照alphabeta（一开始还不知道怎么说）排序再对整个dict排序，使得有公共prefix的单词gruop到一次，可以减少一些比较的次数。然后让我再接着优化，然后我就懵了，然后就GG了。



'''


# 可以预处理。 用dp。 2**26 = 67108864，  67 M 不到。 比较小。 可以接受
#26字母。每个字母存在不存在， 共 2**26 种可能. 每种可能找到最长的长度

'''
这道题有一个暴力预处理的方法，需要理解位运算。

先把单词表示成int(位图），比如一个单词abc，那么和它配对可能的位表其实是111前面有23个0 (000...000111)，表示只有abc出现。这样每个单词其实把把出现的字母标为1，得到了一个int。
我们状态也用int来表示，我们用位(bit)1来表示可以出现哪些字母，0表示这些字母不能出现
重要的是关于这个int的理解，这个int里为1的位表示和它配对的单词可以出现的字母。
'''
#http://www.quora.com/Given-a-dictionary-of-words-how-can-we-efficiently-find-a-pair-words-s-t-they-dont-have-characters-in-common-and-sum-of-their-length-is-maximum

'''
我们的首先把单词对应成int状态，再把每个状态的最长单词算出来就好了，关键是怎么算。
可以理解为dp,或者递推。
（1）第1步。 对所有的状态（共2^26个） 初值 dp[] 先给  For each set S of letters, find the longest word that consists of exactly those letters.
（2）第二步。  find the longest word that consists of at most those letters
 递推关键部分:    ( set bit 从少到多的递推。)
 我自己写的。  dp[x] = max([dp[y]  for y that that remove 1 less set bit from x ] + [dp[x]])

for each x from 1 to 2^26 - 1  (say x has N set bits)
       for each y that set bits number is N-1:
            dp[x] = max(dp[x], dp[y])
'''

'''
Our algorithm will consist of three steps:

    For each set S of letters, find the longest word that consists of exactly those letters.
    For each set S of letters, find the longest word that consists of at most those letters (i.e., some letters may be unused, but you cannot use a letter that does not belong to S).
    最后一步：
    For each word w, compute length(w) * length(longest word out of letters not in w) and pick the maximum.

    有了这张表再遍历一次全部单词，对每个单词对应的int x，

    因为可以出现的实际上是x中那些为0的bit，我们需要对它取反。 所以最终
max(length of word * dp[(~x) & ((1 << 26) - 1)]) 为所求   #取最低25位



'''
#  O(n)




'''
少一个1的状态已经算好了，形象地说，我要枚举ABCDE的全部子集的最优值，它其实等于BCDE、ACDE、ABDE、ABCE、ABCD的子集合（这些其实即使y)的最优以及全集ABCD本身(这个状态是x)的值中的最优值。
'''