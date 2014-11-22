# encoding=utf-8
'''
Implement the integral part logn base 2 with bit manipulations

int integralPartOfLog(unsigned int n)
{

    int ret = 0;

    while (n > 0) {
        n = n>>;1;
        ret++;
    }

    return ret-1;
}
'''
class Solution:
    def integralPartOfLog(self, n):
        ret = 0
        while n>0:
            n = n>>1
            ret+=1
        return ret-1