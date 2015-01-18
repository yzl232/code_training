# encoding=utf-8
# BITMAP，的位运算，应该是怎么左右对调。
'''
result = (n & 0x0000FFFF << 16) | (n & 0xFFFF0000 >> 16);
return result;.
'''