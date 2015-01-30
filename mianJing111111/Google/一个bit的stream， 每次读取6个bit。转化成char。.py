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
    def to6(self, arrByte):  # # 8+8+8 =>  6, 2+4, 4+2, 6  这行先写好。 容易糊涂
        ret = []  #中间两行难写， 先写好框架  chr(  ()| ()   )
        for i in range(0, len(arrByte)-2, 3):  # -3, -2, -1    #注意把高位置为空
            ret+=[chr(arrByte[i]>>2),
                  chr(   ((arrByte[i]&0b11)<<4) |  ((arrByte[i+1])>>4)    ),
                   chr(  ((arrByte[i+1]&0b1111)<<2) |  (arrByte[i+2]>>6) ),
                   chr( arrByte[i+2]&0b111111  ) ]

# 关于corner case的处理。  stream  cnt byte(length of arrByte) % 3.  如果余数0. 不管。 余数1. 补上2个0. 余数2， 补上一个0