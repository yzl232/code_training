# encoding=utf-8
'''
int i = -1;
i = i >>> 1;

//This will shift the singed bit to right by 1 and hence making the value 2147483647
'''

#逻辑右移就是无视符号

'''


>> is arithmetic shift right, >>> is logical shift right.

In an arithmetic shift, the sign bit is extended to preserved the signedness of the number.

For example, -2 in 8 bits would be 11111110 (because the most significant bit has negative weight). Shifting it right one bit using arithmetic shift would give you 11111111, or -1. Logical right shift, however, does not care that the value could possibly represent a number; it simply moves everything to the right and fills in from the left with 0s. Shifting our -2 right one bit using logical shift would give 01111111.

'''