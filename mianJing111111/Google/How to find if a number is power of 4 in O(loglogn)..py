# encoding=utf-8
#How to find if a number is power of 4 in O(loglogn).
'''
How to find if a number is power of 4 in O(loglogn).
'''

#O(1)
# G家考过几次。
'''
bool isPowerof4(int i) {
    return ((i & 0xAAAAAAAA) == 0 && (i&(i-1)) == 0 && i!=0);
}

100
10000
'''

#power of 4特点：在偶数位有一个1.
#1 奇数位   # i & 0xAAAAAAAA   第一个式子解决了。
# 2  一个set bit.  后面都是0.  i&(i-1)解决了。 只有


'''

With O(log(N)) memory you can do faster, O(log(log(N)). Precompute the powers of 3 and then do a binary search on the precomputed values.

'''