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


'''
#这种题目对用python的人比较难
#下面是错的。 看错了题意
#实际上是reverse
class Solution4:
    def flip(self, arr):
        for i in range(len(arr)):
           arr[i] = (arr[i]>>4) | (arr[i]&0b1111<<4)   #这里右移不需要事先


class Solution:
    lookUp=[ 0b0000, 0b1000, 0b0100, 0b1100,
   0b0010, 0b1010, 0b0110, 0b1101,
   0b0001, 0b1001, 0b0101, 0b1101,
   0b0011, 0b1011, 0b0111, 0b1111]
    def reverse(self, arr):
        for i in range(len(arr)):
           arr[i] = (self.lookUp[arr[i]>>4]) | (self.lookUp[(arr[i]&0b1111)]<<4)  #低位麻烦一些。  高位方便一些。

'''
//Index 1==0b0001 => 0b1000
//Index 7==0b0111 => 0b1110
//etc
uint8_t lookup[16] = {
   0b0000, 0b1000, 0b0100, 0b1100,
   0b0010, 0b1010, 0b0110, 0b1101,
   0b0001, 0b1001, 0b0101, 0b1101,
   0b0011, 0b1011, 0b0111, 0b1111 };

uint8_t reverse(uint8_t n) {
   // Reverse the top and bottom nibble then swap them.
   return (lookup[n&0b1111] << 4) | lookup[n>>4];
}
'''

