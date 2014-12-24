# encoding=utf-8
'''
A soda water machine,press button A can generate 300-310ml, button B can generate 400-420ml and button C can generate 500-515ml, then given a number range [min, max], tell if all the numers of water in the range can be generated.
'''
#很特别的dp

class Solution:
    def generate(self, minV, maxV):
        dp = [False for i in range(maxV+1)]
        for i in range(300, 516):
            if 300<=i<=310 or 400<=i<=420 or 500<=i<=515:  dp[i] = True
        for i in range(516, maxV+1):
            if not dp[i]:
                for j in range(300, 311):
                    if dp[i-j]:
                        dp[i] = True
                        break
            if not dp[i]:
                for j in range(400, 421):
                    if dp[i-j]:
                        dp[i] = True
                        break
            if not dp[i]:
                for j in range(500, 516):
                    if dp[i-j]:
                        dp[i] = True
                        break
        return False not in [x for x in dp[minV:maxV+1]]
s = Solution()
print s.generate(700, 721)