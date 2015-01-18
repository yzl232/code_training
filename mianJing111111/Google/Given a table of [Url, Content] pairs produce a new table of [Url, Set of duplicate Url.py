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
        d = {}
        for x, c in arr:
            if c not in d: d[c]=[]
            d[c].append(x)
        for x in d:
            d[x].pop(0)
        return d