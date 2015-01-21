# encoding=utf-8
'''
unsigned int swapBits(unsigned int x)
{
    // Get all even bits of x
    unsigned int even_bits = x & 0xAAAAAAAA;

    // Get all odd bits of x
    unsigned int odd_bits  = x & 0x55555555;

    even_bits >>= 1;  // Right shift even bits
    odd_bits <<= 1;   // Left shift odd bits

    return (even_bits | odd_bits); // Combine even and odd bits
}
'''
def swapOddEvenBits(x):
    return  ((x&0xaaaaaaaa)>>1) | ((x&0x55555555)<<1)