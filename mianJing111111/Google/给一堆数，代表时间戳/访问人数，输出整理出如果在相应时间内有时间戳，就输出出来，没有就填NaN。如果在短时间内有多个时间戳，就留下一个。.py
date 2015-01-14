# encoding=utf-8
'''
给一堆数，代表时间戳/访问人数，输出整理出如果在相应时间内有时间戳，就输出出来，没有就填NaN。如果在短时间内有多个时间戳，就留下一个。


就是比方说有几台机器，平均每100ms打印出一个时间戳和一个访问人数的计数。但是时间不是很精确。有的时候早一点有的时候晚一点。有的时候没有访问人数就不打印出来

现在进行一下统计，每个时间段留下一条数据，如果在短时间内有多条数据，就留下一条；如果那个时间段里没有数据，就生成一条NaN。


sampling interval: 100
input sequence:
timestamps value
1012 7
1102 5
1095 3
1199 10
1405 8
output sequence:
timestamps value
1012 7
1102 5 (or 1095 3)
1199 10
1300 NaN
1405 8


follow up就是问complexity。问了好多，都说我自己定义就好，比方说怎么叫短时间，从什么时候开始计算。比较烦这样的题啊，需求都不是很明确的样子。


我说的是空间复杂度O(1), 时间复杂度是O(n)
'''


class Solution:
    def solve(self, arr, x):
        if not arr: raise  ValueError
        pre = arr[0][0]
        print pre, arr[0][1]
        for i in range(1, len(arr)):
            a, b  = arr[i]
            if a-pre<=x/2: continue
            elif x/2<a-pre<x*1.5:
                print a,b
            else:
                while a-pre>x*1.5:   #贪心算法
                    pre+=100
                    print pre, 'NaN'
                print a, b
            pre = a
s = Solution()
s.solve([[1012, 7],
[1102, 5],
[1095, 3],
[1199, 10],
[1405, 8]], 100)

