# encoding=utf-8
#swap alternate bits of a given number
'''
#swap alternate bits of a given number
'''
def swapOddEvenBits(x):
    return  ((x&0xaaaaaaaa)>>1) | ((x&0x55555555)<<1)