# encoding=utf-8
'''
https://www.youtube.com/watch?v=sqPTR_v4qFA
先熟悉一下。

http://www.cnblogs.com/powertoolsteam/archive/2010/09/20/1831638.html

看起来很复杂，总结起来如下：

ASCII码（U+0000 - U+007F），不编码

其余编码规则为

    •第一个Byte二进制以形式为n个1紧跟个0 (n >= 2), 0后面的位数用来存储真正的字符编码，n的个数说明了这个多Byte字节组字节数（包括第一个Byte）
    •结下来会有n个以10开头的Byte，后6个bit存储真正的字符编码。
    因此对整个编码byte流进行分析可以得出是否是UTF8编码的判断。


filename = 'inputFile'
valid_utf8 = True
try:
    filename.decode('utf-8')
except UnicodeDecodeError:
    valid_utf8 = False

UCS-4 range (hex.) UTF-8 octet sequence (binary)
　　0000 0000-0000 007F 0xxxxxxx
　　0000 0080-0000 07FF 110xxxxx 10xxxxxx
　　0000 0800-0000 FFFF 1110xxxx 10xxxxxx 10xxxxxx
　　0001 0000-001F FFFF 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
　　0020 0000-03FF FFFF 111110xx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
　　0400 0000-7FFF FFFF 1111110x 10xxxxxx ... 10xxxxxx
　　utf-8的编码步骤：（与本题目无关）
　　1) 首先确定需要多少个8bits(octets)
　　2) 按照上述模板填充每个octets的高位bits
　　3) 把字符的bits填充至x中，字符顺序：低位→高位，UTF8顺序：最后一个octet的最末位x→第一个octet最高位x
　　根据UTF8编码,最多可由6个字节组成,所以UTF8是1-6字节编码组成



最多6个byte

UTF-8 encoding scheme is described below:

0XXXXXXX = this is the entire rune
10XXXXXX = this is a continuation of the rune from the previous byte
110XXXXX = this is the start of a 2-byte rune.
1110XXXX = this is the start of a 3-byte rune.
11110XXX = this is the start of a 4-byte rune.
111110XX = this is the start of a 5-byte rune.
1111110X = this is the start of a 6-byte rune.

For example, a 3-byte rune would be 1110XXXX 10XXXXXX 10XXXXXX.

Write a function that decides whether a given byte array (or string) is
valid UTF-8 encoded text.
'''
#虽然只是普通的O(n)。 但还是有点难。
class Solution:  #比较大小
    def isUTF_8(self, s):  #string
        nBites = 0;     bAllAscii =True #如果全部都是ASCII, 说明不是UTF-8.  这是一种特殊情况。 单独列出。
        for ch in s:
            chVal = ord(ch)
            if chVal>>7==1:    bAllAscii = False   #判断是否ASCII编码,如果不是,说明有可能是UTF-8,ASCII用7位编码,但用一个字节存, 0x80=10000000
            if nBites==0:#如果不是ASCII码,应该是多字节符.  每次完了需要重新计算字节数  后面对应nBites-=1
                if chVal>>7 ==0:  continue
                elif chVal>>6==0b10:    return False   #比较奇怪。  0b10xxxxx不是valid的. 10xxxxxx只能是多字节符的非首字节,
                elif chVal>>5==0b110:    nBites=2
                elif chVal>>4==0b1110:    nBites=3
                elif chVal>>3==0b11110:    nBites=4
                elif chVal>>2==0b111110:   nBites=5
                elif chVal>>1==0b1111110:   nBites=6
                nBites-=1   #
            else:
                if chVal>>6!=0b10: return False#//多字节符的非首字节,应为 10xxxxxx
                nBites-=1
        return nBites==0 and not bAllAscii  #如果全部都是ASCII, 说明不是UTF-8   #违返规则
s = Solution()
print s.isUTF_8("sfewfwef")
print s.isUTF_8("sssewfew的萨芬")