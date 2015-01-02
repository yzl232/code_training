# encoding=utf-8
'''
写一个函数生成满足下面三个条件的integer
1. 非负
2. 不能有重复数字
3. 递增，既后面产生的比前面产生的要大

我问要一次性全部生成所有数字还是每呼叫一次函数产生一个，他让我先写一次性产生
全部的，这个不难，backtracking，follow up是假设现在给一个符合条件的数字，如
789，返回下一个（比输入大但是最小的）数字，790。一开始我没思路，说很多edge
case，然后多观察几个例子后发现有些规律，说出来后他说看起来不错，然后举了几个
例子让我模拟跑一遍，没有问题，他说ok，不用写code了，正好也到时间了

'''
#  1~10**10.  然后除去有重复的。
#9876543210
#暴力法
class Solution:
    def find(self):
        return [i for i in range(10**10) if len(str(i))==len(set(str(i)))]

    def nextN(self, n):
        i = n+1
        while True:
            s = str(i)
            if len(s)==len(set(s)):   return i
            i+=1

#因为范围有限的。 0~9876543210。 所以暴力法是可以的。
s = Solution()
cur = 15240
for i in range(100):
    cur= s.nextN(cur)
    print cur