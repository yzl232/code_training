# encoding=utf-8
'''
Given a table of [Url, Content] pairs produce a new table of [Url, Set of duplicate Url

Example Input:
a.com => <html>a</html>
b.com => <html>b</html>
c.com => <html>c</html>
d.com => <html>a</html>
e.com => <html>a</html>

Example Output:
a.com => [d.com, e.com]
b.com => []
c.com => []
'''
class Solution:
    def solve(self, arr):
        d = {c:[] for x, c in arr}   #题目输出只有a, b, c。 没有d， e  说明是以html  val作为指标。
        for x, c in arr:
            if c!=x:  d[c].append(x)   #除去本身
        return d