# encoding=utf-8
#就是比如说给定一个数 n, 一个digit k (k = 0,1,....9)  从 0-n 之间的数字 （十进制）里面 k 出现的次数的和 （每一位上）
#Count the number of digits that in all legal positive numbers below N.; f



class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum((n/base+7)/10*base + (n/base%10==2)*(n%base+1) for base in (10**i for i in range(len(str(n))+1)))

'''
152222        15*1000+223       n%base+1
153222        16*1000
150222        15*1000
                n/base/10
千位

def countDigitOne(self, n):
    ones = 0
    m = r = 1
    while n > 0:
        ones += (n + 8) / 10 * m + (n % 10 == 1) * r
        r += n % 10 * m
        m *= 10
        n /= 10
    return ones

class Solution(object):  # http://blog.csdn.net/xudli/article/details/46798619
    def countDigitOne(self, n):  # http://www.cnblogs.com/grandyang/p/4629032.html
        ret, base = 0, 1    #从个位到十位到百位。  m不断乘以10
        while base <= n:  # 用(x+8)/10来判断一个数是否大于等于2
            a, b = n/base, n%base
            ret += (a + 8) / 10 * base + (a % 10 == 1) * (b + 1)  #判断某一位的一, 整天看,  一个数量位. 结果为x/10数量级
            base *= 10
        return ret

digit >=3:    (a/10 + 1) * base
digit ==1:    a/10*base + (b+1)
digit ==0:   a/10*base

以算百位上1为例子:   假设百位上是0, 1, 和 >=2 三种情况:

    case 1: n=3141092, a= 31410, b=92. 计算百位上1的个数应该为 3141 *100 次.

    case 2: n=3141192, a= 31411, b=92. 计算百位上1的个数应该为 3141 *100 + (92+1) 次.

    case 3: n=3141592, a= 31415, b=92. 计算百位上1的个数应该为 (3141+1) *100 次.

以上三种情况可以用 一个公式概括:

(a + 8) / 10 * m + (a % 10 == 1) * (b + 1);

'''

'''
cc150上类似的题目




 第二题同时也是微软编程之美中的那个count 1的个数的类似题。这种题找好了规律就好做。
'''


'''
Write a method to count the number of 2s that appear in all the numbers between 0 and n (inclusive).
EXAMPLE
Input: 25
Output: 9 (2,12,20,21,22,23, 24 and 25. Note that 22 counts for two 2s.)


f(513) = 5 * f(99) + f(13) + 100            # (首位。 200~299 一共100个)
f(279) = 2 * f(99) + f(79) + 79 + 1
'''

#把2变成k。就是k了
class Solution:
    def count2s(self, n):
        if n==0: return 0
        power = 1
        while 10*power<n: power*=10
        first, rem  = n/power, n%power
        cnt = 0
        if first>2: cnt=power
        elif first==2: cnt=rem+1   #+1, -1就是inclusize, exclusive的区别
        return cnt + first*self.count2s(power-1)+self.count2s(rem)