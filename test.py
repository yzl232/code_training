
class Solution2:
    def find_Ancestor2(self, p, q):
        h1 = self.getHeight(p)
        h2 = self.getHeight(q)

        if h1> h2:
            h1, h2 = h2, h1
            p, q = q, p

        # h2 is bigger
        dh = h2 - h1
        for i in range(dh):
            q = q.parent
        while p and q:
            if p == q: return p
            p = p.parent
            q = q.parent

    def getHeight(self, p):
        h = 0
        while p:
            p = p.parent
            h+=1
        return h
# O(1) and O(h)
#直接写最优解就好了。  第一种解法提一下就好。