class Solution:
    def de_bruijn(self):
        self.ret = list('0000'); self.visited = set(['0000'])
        self.dfs(); return self.ret

    def dfs(self):
        if len(self.ret)==10003: return True
        for ch in '0123456789':
            cur = ''.join(self.ret[-3:]+[ch])
            if cur in self.visited: continue
            self.ret.append(ch); self.visited.add(cur)
            if self.dfs(): return True
            self.ret.pop(); self.visited.remove(cur)
        return False