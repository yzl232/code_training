# encoding=utf-8
'''
Given random() that can return 0 or 1 uniformly, implement random_new() that can return 0 with 90%, and 1 with 10%

是rand5, rand7的变种


运行四次就行了吧。
0000~1111
0000到1001的话返回0,1010返回1，其它调用自身
缺点是调用自身的概率会有点大，优点就是不用运行那么多次原函数
不过也不好说，都是tradeoff
'''
class Solution:
    def rand2(self):
        pass

    def rand10(self):
        ret = ''.join(str(self.rand2()) for i in range(4))
        if '0000'<=ret<='1000': return 0
        elif ret == '1001': return 1
        return self.rand10()