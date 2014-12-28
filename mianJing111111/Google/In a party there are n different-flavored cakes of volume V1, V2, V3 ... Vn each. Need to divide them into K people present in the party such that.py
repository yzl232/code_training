# encoding=utf-8
'''
In a party there are n different-flavored cakes of volume V1, V2, V3 ... Vn each. Need to divide them into k people present in the party such that
- Each member of party gets equal volume of cake (say V, which is the solution we are looking for)
- A given member should get a cake of single flavour only i.e. You cannot distribute parts of different flavored cakes to same member.
- Minimum volume of cake gets wasted after distribution so that means a maximum distribution policy
'''
# find largest possible x for each person
#O(n * log((sum(Vi)/m)/eps) )
class Solution:  #因为l基本上是越小越可以符合。 比如 0.0001
    def solve(self, k, v):
        l=0; h=sum(v)+1; accuracy = 0.00001
        while (h-l)>accuracy:
            m = (l+h)/2.0
            if self.works(m, v, k): l=m
            else: h=m
        return l

    def works(self, m, v, k):
        return sum(int(val/m) for val in v)>=k  #注意是int(val/m)。因为不能出现0.5这种情况,.  另外是>=k
s = Solution()
print s.solve(4, [6, 5, 12])
print s.solve(6, [4, 4, 2])