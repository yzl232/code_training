# encoding=utf-8
'''
A soda water machine,press button A can generate 300-310ml, button B can generate 400-420ml and button C can generate 500-515ml, then given a number range [min, max], tell if all the numbers of water in the range can be generated.
'''
#很特别的dp

class Solution:
    def generate(self, minV, maxV):
        canGen=set(range(300, 311)+range(400, 421)+range(500, 516))
        for i in range(maxV+1):  # i从0开始的。
            if i not in canGen:
                for j in canGen:
                    if i-j in canGen:
                        canGen.add(i);  break
            return all(x in canGen  for x in range(minV, maxV))
s = Solution()
print s.generate(700, 721)
'''
class Solution:
    def generate(self, minV, maxV):
        dp = [False ] *(maxV+1)
        for i in range(300, 516):
            if 300<=i<=310 or 400<=i<=420 or 500<=i<=515:  dp[i] = True
        for i in range(516, maxV+1):
            if not dp[i]:
                for j in range(300, 311):
                    if dp[i-j]:
                        dp[i] = True;  break
            if not dp[i]:
                for j in range(400, 421):
                    if dp[i-j]:
                        dp[i] = True;   break
            if not dp[i]:
                for j in range(500, 516):
                    if dp[i-j]:
                        dp[i] = True;   break
        return False not in [x for x in dp[minV:maxV+1]]
'''
