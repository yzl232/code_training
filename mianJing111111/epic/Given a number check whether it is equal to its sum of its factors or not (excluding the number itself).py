# encoding=utf-8
class Solution:
    def equalToallFactors(self, n):
        factors = [1]
        for i in range(2, int(n**0.5)+1):
            if n%i==0:  factors+=[i, n/i]
        factors = list(set(factors))
        return n==sum(factors)




s = Solution()
print s.equalToallFactors(40)
