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
   compare a,  a+1
elif a>b:
    compare a, a-1
else: return a



'''