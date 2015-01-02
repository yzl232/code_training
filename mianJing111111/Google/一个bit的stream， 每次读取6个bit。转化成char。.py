# encoding=utf-8
'''
一个bit的stream， 每次读取6个bit。转化成char。

但是写那个bit流的时候，输入是一个Byte array
然后我在那里想办法算offset做位操作，最后code竟然没有finish。
'''


'''
Well, every 3 bytes, you end up with four characters. So for one thing, you need to work out what to do if the input isn't a multiple of three bytes. (Does it have padding of some kind, like base64?)
'''

class Solution:
    def to6(self, arrByte):
        ret = []
        for i in range(0, len(arrByte), 3):
            ret.append(chr(arrByte[i]>>2)  )
            ret.append(chr(   ((arrByte[i]&0b11)<<4) |  ((arrByte[i+1])>>4)    ))#注意把高位置为空。
            ret.append(chr(  ((arrByte[i+1]&0b1111)<<2) |  (arrByte[i+2]>>6) ))
            ret.append(chr( arrByte[i+3]&0b111111  ))