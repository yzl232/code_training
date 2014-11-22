# encoding=utf-8
import  time
seed = 0
class Solution:
    def generateRandom(self, n):
        global seed
        seed +=int(time.time())
        return seed%n
s= Solution()

