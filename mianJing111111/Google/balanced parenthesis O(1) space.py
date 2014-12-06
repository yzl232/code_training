# encoding=utf-8
'''
1.括号匹配
一开始用了O(N)的空间, 后来要求用O(1)的空间完成.

第一题就是左括号的个数和右括号个数一样并且符合我们平时的逻辑。
例如：（）， （（））， （）（） 都是有效匹配， 返回true；
例如：（（）， ）（， （））（ 都是无效的， 返回false；

'''

#只有一种括号。 可以用巧妙的count办法来做
class Solution:
    def valid(self, s):
        cnt = 0
        for i in s:
            if i=='(': cnt+=1
            else: cnt-=1
            if cnt<0: return False    #小于0则不平衡
        return cnt==0         #和为0则平衡