# encoding=utf-8  #
class Solution:
    def calculateAngle(self, hh, mm):
        angle = abs(360.0/60*mm-(hh*30+mm*30.0/60)) #每60分钟30度。 每分钟1度
        return min(angle, 360-angle)

s = Solution()
print s.calculateAngle(12, 15)