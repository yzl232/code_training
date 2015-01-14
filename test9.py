# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def __init__(self):
        self.offset = 0
        self.bufsize = 0 #If bufsize > 0, that means there is partial data left in buffer .
        self.tmpBuffer = [None for i in range(4)] # 我们直接复制这里就好。不用call read4k
        
    def read(self, buf, n):
        count = 0; flag = True
        while n > count and flag:#tmp的作用就是判断是不是4。
            if self.bufsize!=0:  tmpN = self.bufsize
            else:
                tmpN = read4(self.tmpBuffer)
                if tmpN<4: flag = False
            byteN = min(tmpN, n-count)   #结束的2个指标 。  1 tmp!=4.   或者n<=count 读完了。
            buf[count:count+byteN]= self.tmpBuffer[self.offset:self.offset+byteN]
            self.offset = (self.offset+byteN) % 4  #  因为我们目标是读n个。
            self.bufsize = tmpN - byteN  #就是判断有没有残余。   也就是n-count < tmpN吗？
            count+=byteN
        return count        