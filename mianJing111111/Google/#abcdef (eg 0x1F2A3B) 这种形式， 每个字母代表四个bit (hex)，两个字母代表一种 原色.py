# encoding=utf-8
'''
上来直接上题，题目有些绕。CSS里面表示颜色用
#abcdef (eg 0x1F2A3B) 这种形式， 每个字母代表四个bit (hex)，两个字母代表一种
原色
比如 ab = R, cd = G, ef = B (每种原色整个是0-255间的一个数字)
现在需要压缩空间改#abcdef 为 #xyz
实际上#xyz = #xxyyzz,所以减小一半，问怎么找到最好的压缩让
（ab-xx）^2 + (cd - yy)^2 + (ef - zz)^2 最小

这题其实数学上很简单因为三个维度是分开的，其实就是找#ab到#xx的压缩。




 a的权重
更大， x应该很接近a， 实际上 x = a, a - 1 , or a + 1。


a > b 时 x = a, a- 1，

a < b时 x = a, a + 1


'''
#出现过几次


#x=只能是a, a-1, a+1 三种

'''
The second problem for Google:

For RGB, ab is 16*a + b; xx is 16*x + x

The problem is to minimize |17x - 16a - b|^2, x from 0 to 15.

Only need to consider x = a - 1,  a, or a + 1, depends on the value of b.

So we only need to compare |a - b|, |a - b - 17| and |a - b + 17|.

Note that -15 <= a - b <= 15;

we can get the closest solution: if a - b >= 9
, we should choose x = a - 1;

if a - b <= -9, we should choose x = a + 1;


otherwise we should choose x = a.

'''



#结论如下。 注意是For RGB, ab is 16*a + b; xx is 16*x + x
'''
if a<b:
   compare x=a,  x=a+1
elif a>b:
    compare x=a, x=a-1
else: return a

#优先考虑高位。

'''


class Solution:
    def solve(self, arr):
        assert len(arr)%2==0
        ret = arr[:]
        for i in range(len(arr), 2):
            a=arr[i]; b=arr[i+1]
            t = min(  (self.cal(a, b, x), x) for x in [a-1, a, a+1]  )
            ret[i]=ret[i+1]=t[1]
        return ret

    def cal(self, a, b,x ):
        return abs(16*a+b-17*x)



'''
. 有某种颜色的表示为6位十六进制数组成的数，比如ABCDEF。两个颜色间的“距离”定义如下：
ABCDEF 和 HIJKMN的距离为：
-(AB-HI)^2 - (CD-JK)^2 - (EF-MN)^2

那么，给定一个颜色A，比如123456，求离该颜色最近的颜色B，“最近”意思是两个颜色距离最接近零。
B的形式必须为XXYYZZ，即12,34,56位要分别相等。

比如，A = 123456，那么B = 113355。
'''