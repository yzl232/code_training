import random

class Solution:
    def randomize(self, arr):
        n = len(arr)
        for i in range(n-1, -1, -1):
            j = random.randint(0, i)
            arr[j], arr[i] = arr[i], arr[j]