# encoding=utf-8
#Flip a monochrome bitmap around its centre-line, where input is: char *bytes, int width, int height
#又是这种pixel的题目。 日。
#一般就是每个像素存为一个bit。  8个像素存为一个byte， 或者8个像素存为一个char.
'''
Flip a monochrome bitmap around its centre-line, where input is: char *bytes, int width, int height .

Example:
Input
0101 0110
1111 0011

Output
0110 1010
1100 1111



We are given array of characters. Let there be n characters, each row has 8 bits. 8 bits of each char are to be flipped around its centre.

Ex:
0011 | 0101

will be flipped (swap the nibbles) to

0101 | 0011
'''
#这种题目对用python的人比较难
class Solution:
    def flip(self, arr):
        for i in range(len(arr)):
           arr[i] = (arr[i]>>4) | (arr[i]<<4)
