# encoding=utf-8
'''
给你一个password 假定6位，
有个function 每call 一次就给你一个triplet 是password 里的随即三位，order不变
。比如google, 可能返回， ggl, goe, oog, ool, ........
问如何最有效破译这个密码，写code.

也就是排列了。  order不变


频率统计法
ABCDEF，每次triplet XYZ
记录X的频率，Y的频率，Z的频率
X可能包含了ABCD，A出现的频率是10/20,B:6/20,C:3/20,D:1/20
ABCD如果都相同，那么就是20
ABCD如果其中2个字母相同，就是16，13，11，9，7，4
3个字母相同，结果是19,14,10,17
都不相同就是10,6,3,1
注意10可能是abbb或者abcd，那么用Y的频率来判断哪种情况。


假设a b c d e f 是password字符的位置，而 x y z 是返回字符的位置。
x 可能是{a,b,c,d}
y 可能是{b,c,d,e}
z 可能是{c,d,e,f}
所有的组合是C(6,3) = 20种。
每个字符pos出现的概率表如下：
       x        y         z
a    10/20      0         0         都是10个
b     6/20     4/20       0       都是10个
c     3/20     6/20      1/20   都是10个
d     1/20     6/20      3/20
e      0       4/20      6/20
f      0        0        10/20

如果密码是abcdef，那么以a开头的bucket应该是 C(5, 2) = 10个 (剩下的5个选2个)。以b开头的buckt应该是C(4, 2) = 6个，以c开头的是3个，以d开头的是1个…. from this, we know the probability of the occurrance of each letter.
'''



'''
频率统计法
ABCDEF，每次triplet XYZ
记录X的频率，Y的频率，Z的频率
X可能包含了ABCD，A出现的频率是10/20,B:6/20,C:3/20,D:1/20
ABCD如果都相同，那么就是20
ABCD如果其中2个字母相同，就是16，13，11，9，7，4
3个字母相同，结果是19,14,10,17
都不相同就是10,6,3,1
注意10可能是abbb或者abcd，那么用Y的频率来判断哪种情况。

这样可以解出a, b ,c ,d.

e, f

程序的写法：

3中情况：
ABCD如果都相同，那么就是20
ABCD如果其中2个字母相同，就是16，13，11，9，7，4
3个字母相同，结果是19,14,10,17
都不相同就是10,6,3,1
注意10可能是abbb或者abcd，那么用Y的频率来判断哪种情况。
'''