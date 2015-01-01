# encoding=utf-8
'''
very large bytestream (PB)
synchronization algorithm

given:
unsigned char read_byte(); ← side effect that it advances a byte pointer in the stream

write:
unsigned char read_sync_byte(); ← may result in >1 calls to read_byte()

remove byte '03' from the stream if the stream is in pattern 00 00 03

Example:

read_byte():
00 0f 42 17 00 00 03 74 00 00 00 00 14 ...

read_sync_byte():
00 0f 42 17 00 00 74 00 00 00 00 14 ...
'''


#在stream里边删除03.  可以用finite state machine。 也可以用count
# count 00数目要更加简单一些
#另外注意这个是byte。 每个byte如题目所说是2个数字.  看来意思是十六进制了。
class Solution:
    def arr(self, arr):
        cnt=0; ret = ''
        for byte in arr:
            if byte=='03' and cnt>=2:  cnt=0
            elif byte =='00':
                cnt+=1
                ret +=byte
            else:
                cnt=0
                ret+=byte
        return ret