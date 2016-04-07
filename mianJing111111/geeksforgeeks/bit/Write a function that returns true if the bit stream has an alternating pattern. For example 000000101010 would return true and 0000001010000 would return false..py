# encoding=utf-8
'''
Write a function that returns true if the bit stream has an alternating pattern. For example 000000101010 would return true and 0000001010000 would return false.
'''

#直接这样：  b=a>>1;      if a&b==0 and a!=0: returnTrue

'''
bool patternCheck(int a)
{
int b=a>>1;
/*if a=000000101010 then b=0=00000010101,,,,rightshift of a by 1*/
//now xor of a and b
int n=(a^b)+1;//n is in 2^n format if alternate bits are there
if(n & (n-1)) == 0) return true;
return false;
}
'''

def check(a):
    n = a^(a>>1)+1  # n=a&b
    return n&(n-1)==0   #简单的说，就是是不是2^n次方？  只有一个set bit