# encoding=utf-8
'''
Write the following function
void drawLine(byte[] img, int len, int wid, int r, int x1, int x2)
such that you draw a line from x1 to x2 at row r.
len is the length and wid is the width of the image/canvas.
Setting a pixel on to draw the line is to set the corresponding bit on the img array
Each byte corresponds to 8 pixels, that is each pixel is a bit in the array
'''
#意思就是每个像素是用byte来存的。 并不是二维矩阵。  一维矩阵。 压缩了8倍， 就是byte array

'''
ByteArray is an extremely powerful Class that can be used for many things related to data manipulation, including (but not limited to) saving game data online, encrypting data, compressing data, and converting a BitmapData object to a PNG or JPG file.
'''
#http://www.programcreek.com/2009/02/java-convert-image-to-byte-array-convert-byte-array-to-image/

#比较难的。  byte array都比较难

#看到几次了

class Solution:
    def drawLine(self, byte, wid, r, x1, x2):
        startBit = (r-1)*wid+x1
        endBit = (r-1)*wid+x2
        x1, y1 = startBit/8, startBit%8
        x2, y2 = endBit/8, endBit%8
        for i in range(x1+1, x2):
            byte[i] |= 0xFF
        for i in range(y1):
            byte[x1] |= 1<<(8-i)
        for i in range(y2):
            byte[x2] |=1<<i
#考的是bit运算
'''
mitbbs
在2D的screen上划线(x1, y) 到 (x2,y)，其中知道screen的宽W，高H。每
个坐标(x, y)对应memory的一个bit，给定memory的初始地址，写代码实现。
'''