# encoding=utf-8
import  time
seed = 0
class Solution:
    def generateRandom(self, n):
        global seed
        seed =(seed+int(time.time()) ) %n
        return seed
s= Solution()

