# encoding=utf-8
'''
How to remove duplicate lines in a large text file? I think it's easy to find duplicate lines, but how do we efficiently remove them from the file?
'''


# 小的话。 hashtable

'''
We can use hashing + hashing + hashing approach.
First hash will be based on number of characters in line
Second hash will be number of words in the line
third will be hash of words and now we can store line here.

When a new line comes, it will pass all three hashes and if comes into same bucket then we can compare lines.
using these 3 hash (or filters) we can minimize the chances of clashing lines.
'''


#如果顺序不重要的话。 就是老办法。  用hash  %1000  split成1000个部分。   然后去重。
# else  bloom filter