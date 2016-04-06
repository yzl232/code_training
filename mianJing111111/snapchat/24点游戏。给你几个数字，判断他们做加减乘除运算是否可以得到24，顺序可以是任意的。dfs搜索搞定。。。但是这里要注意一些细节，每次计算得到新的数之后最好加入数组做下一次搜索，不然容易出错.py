'''
24点游戏。给你几个数字，判断他们做加减乘除运算是否可以得到24，顺序可以是任意的。dfs搜索搞定。。。但是这里要注意一些细节，每次计算得到新的数之后最好加入数组做下一次搜索，不然容易出错
'''

# encoding=utf-8

'''
24点游戏。给你几个数字，判断他们做加减乘除运算是否可以得到24，顺序可以是任意的。dfs搜索搞定。。。但是这里要注意一些细节，每次计算得到新的数之后最好加入数组做下一次搜索，不然容易出错
'''
'''
24  return True

2, 12  return True

13 return False

2, 48  return True
'''
#写了一遍。 比较纯粹的dfs。 
class Solution:
    def solve(self, arr):
        self.ret = False
        
        def dfs(cur, rest):
            if self.ret: return
            if not rest:
                if cur == 24: self.ret = True
                return
            for x in rest:
                t = rest[:]; t.remove(x)
                dfs(cur+x, t)
                dfs(cur-x, t)
                dfs(cur*x, t)
                dfs(cur/x, t)
                
        for x in arr:
            t = arr[:];  t.remove(x)
            dfs(x, t)
        return self.ret

s = Solution()
print s.solve([2, 12])
print s.solve([13])
print s.solve([48, 2])