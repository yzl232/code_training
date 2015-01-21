# encoding=utf-8
'''

Rotate bits of a number

Bit Rotation: A rotation (or circular shift) is an operation similar to shift except that the bits that fall off at one end are put back to the other end.

In left rotation, the bits that fall off at left end are put back at right end.

In right rotation, the bits that fall off at right end are put back at left end.



n = 11100101 by 3 makes n = 00101111 (Left shifted by 3 and first 3 bits are put back in last ).

int leftRotate(int n, unsigned int d)
{
   /* In n<<d, last d bits are 0. To put first 3 bits of n at
     last, do bitwise or of n<<d with n >>(INT_BITS - d) */
   return (n << d)|(n >> (32 - d));
}

/*Function to right rotate n by d bits*/
int rightRotate(int n, unsigned int d)
{
   /* In n>>d, first d bits are 0. To put last 3 bits of at
     first, do bitwise or of n>>d with n <<(INT_BITS - d) */
   return (n >> d)|(n << (32 - d));
}

'''
def rightRotate(x, k):
    return x>>k | x<<(32-k)

# 比如k=5,  那5位要移动到最左边。