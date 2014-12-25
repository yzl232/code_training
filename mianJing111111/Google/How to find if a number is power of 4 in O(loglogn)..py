# encoding=utf-8
#How to find if a number is power of 4 in O(loglogn).
'''
How to find if a number is power of 4 in O(loglogn).
'''

#O(1)

'''
bool isPowerof4(int i) {
    return ((i & 0xAAAAAAAA) == 0 && (i&(i-1)) == 0);
}
'''

#power of 4特点：在奇数位有一个1.
#1 奇数位   # i & 0xAAAAAAAA   第一个式子解决了。
# 2  一个set bit.  后面都是0.  i&(i-1)解决了。 只有