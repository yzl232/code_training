# encoding=utf-8
'''
int N，让输出所有的长度为N的valid string的个数，valid string的
定义是由A,B,C三种字母组成，并且在这个string中任意连续的三个字母不能包括A,B,C
三个字母，比如BACCA就不是valid string


增加一个相同字母， 增加一个不同字母
直接用两个数记录前一个位置上，。相同两个字母结尾的为a,不同字母结尾的为b
这样迭代一下
a = a +b;
b = 2*a+b;
初始值为长度为2，所以a=3,b=6，不就可以了吗


x0  x0  __
x0  x1 __
'''
#和黑格子的类似
def triple_free_combinations(n):
    """Return the number of ways to choose n items , subject to the constraint that no colour appears three
    times in a row.    """
    if n == 1:     return 3
    same, dif = 3, 6 #初始化
    for i in range(n - 1):
        same, dif = same+dif, 2*same+dif
    return same+dif