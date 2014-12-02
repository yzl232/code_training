# encoding=utf-8
'''

Given a byte array, which is an encoding of characters. Here is the rule:
    a. If the first bit of a byte is 0, that byte stands for a one-byte
character
    b. If the first bit of a byte is 1, that byte and its following byte
together stand for a two-byte character
Now implement a function to decide if the last character is a one-byte
character or a two-byte character
Constraint: You must scan the byte array from the end to the start.
Otherwise it will be very trivial.





Agree 这个算法。
解释一下：
从后向前，如果某一位是0了
那么可以肯定，0后面的不会是2 bytes的第二位。
因为后面都是1，也就是说，0后面的那位必然是2 bytes的第一位。
这个问题就是数有多少个1，如果1是奇数，那么这个就是2bytes的第二位，
否者1byte


没问题.

本题的关键就是从后往前看到第一个0开始的点是个断点.
无论那个0开头自己解释自己还是跟它前面的那个走,(不可能跟后面走)

都不影响0开头的后面的那个是个起始字节这个结论.
所以就变成了奇偶问题了.



bool IsLastOneByteChar(unsigned char * bytes, int len)
{
    int leadCount = 0;
    len--;
    bool lastByteIsLead = bytes[len] & 0x80;

    while(len > 0)
    {
        if (bytes[len] & 0x80) leadCount++;
        if (!(bytes[len] & 0x80)) break;
    }

    if (leadCount/2 == 0)
    {
        if (lastByteIsLead)
            return true; //second byte of a 2-byte char
        else
            return false; //single byte char;
    }
    else
    {
        if (lastByteIsLead)
            throw new Exception("invalid string");
        else
            return true; //second byte of a 2-byte char
    }
}

'''