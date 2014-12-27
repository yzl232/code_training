# encoding=utf-8
'''
c = ‘a’
w = “apple”
c covers w, iff w contains c.
c_set = {‘a’, ‘b’, ‘c’, ‘g’}
w_set = {‘apple’, ‘ibm’, ‘cisco’, ‘google’}
c_set covers w_set, iff every w in w_set is covered by some c in c_set.
Given c_set and w_set, Whether w_set is covered by c_set?
'''

#c_set is a set of characters and w_set is a set of words

# basically c_set covers w_set means that all the words in w_set contains at least one character from c_set
'''
1. create 26-bit (using 4 bytes) bit mask where i-th bit is set if i-th character of the alphabet is in c_set. For example, if c_set is {a, b, c, g}, it is like 11100010000.... let's call it cmask

2. For each word, create a similar mask. For "apple", bits for a, p, l, e are set. Let's call it wmask_i for w_i.

Then compute bitwise AND with cmask and each wmask_i. If any of them evaluates to 0, stop there and return false. If every cmask & wmask_i is non-zero, c_set covers w_set.

'''



#G家很喜欢这种字典。  bitmask的题目
#其实brute force来查hashtable一样的。


'''
Follow up: if w_set is fixed say a book, how to determine whether a c_set covers this w_set?
'''
# 除了暴力。没啥好办法。
#small  optimize

'''
 can't really think of any good solutions for the second part. Small optimizations that I can think of are:

1. precompute wmask_i.

2. wmask_1 & wmask_2 & ... & wmask_n indicates characters that appear in all of the words. If cmask & this w_mask is non-zero, c_set covers w_set

3. wmask_1 | wmask_2 | ... | wmask_n indicates all the characters that appear in w_set. If cmask & this wmask is zero, c set doesn't cover w_set.
'''