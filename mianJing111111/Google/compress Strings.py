# encoding=utf-8
'''
Compress Strings
You are given a string FOOFIGHTERS. You have to come up with an algorithm that will compress this string.

You also have to make sure that you are not using extra memory. For example: FOOFIGHTERS will be compressed as FO2FIGHTERS. You should not use another array or bitfield to keep a frequency count for the individual letters.
'''
#微软考过。
#FOOFII    F2FI2
#对于只出现一个的ch， 我们可以反转符号，来标记只出现一次。 对于多次的，可以加上出现次数
# byte array