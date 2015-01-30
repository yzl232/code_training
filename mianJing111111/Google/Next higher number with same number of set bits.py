# encoding=utf-8
#G家。  其实是geeks上面的题目
'''

Next higher number with same number of set bits

Given a number x, find next number with same number of 1 bits in it’s binary representation.

For example, consider x = 12, whose binary representation is 1100 (excluding leading zeros on 32 bit machine). It contains two logic 1 bits. The next higher number with two logic 1 bits is 17 (100012).
'''

'''

To get the next highest number, simply search for the first instance of 01, starting on the right and change this to 10. Then collapse all the 1s to the right of the swapped bits into their least significant positions.

Example:

 ||
00110000 // 0x30 in hex

After swap:

 ||
01010000 // 0x50 in hex

Next, collapse all the 1s to the right of the swapped bits into the least significant positions:

 ||---->
01000001 // 0x41 in hex

To get the previous number, search for the first instance of 10 starting from the right, and replace it with 01. Then collapse all the 0s after the swapped bits in to the least significant positions (alternatively, collapse all the 1s after the swapped bits into their most significant positions).

Example:

    ||
01001001 // 0x48 in hex

After swap:

    ||
01000101 // 0x45 in hex

Next, collapse all the 0s to the right of the swapped bits into the least significant positions:

    ||->
01000110 // 0x46 in hex

Here is a short program that will display both the next higher and lower numbers.


'''
#http://stackoverflow.com/questions/17047290/given-a-number-print-the-next-highest-number-which-has-same-number-of-ones



# 算法是很赞 。但是用string做的。 未必合口味。 不过是个好思路。
# 主要python没有unsigned的数。
class Solution:
    def find(self, x):
        s = list('0'+ bin(x)[2:])
        for i in range(len(s)-1, 0, -1):
            if s[i-1]=='0' and s[i]=='1': break
        print s
        s[i-1], s[i] = s[i], s[i-1]     #找到一个01， 变成10
        l=i+1;  h=len(s)-1     #i右边的降序排列。  。
        while l<h:   #把1移动到后面去
            while l<h and s[l]=='0':l+=1
            while l<h and s[h]=='1':h-=1
            s[l], s[h] = s[h], s[l]
        return int(''.join(s), 2)
s = Solution()
print bin(12)
print s.find(12)
print bin(7)
print s.find(7)
print bin(11)




# lower。只要把0， 1调换。  也就是 把 10  变成01. 然后把0右移动
# i右边的降序。