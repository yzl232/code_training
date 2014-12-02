# encoding=utf-8
'''

Leaders in an array

Write a program to print all the LEADERS in the array. An element is leader if it is greater than all the elements to its right side. And the rightmost element is always a leader. For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.
'''
'''
(Scan from right)
Scan all the elements from right to left in array and keep track of maximum till now. When maximum changes it’s value, print it.
'''
class Solution:
    def leader(self, arr):
        if not arr: return
        result = [arr[-1]]; maxN = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            if maxN<arr[i]: result.append(arr[i])
            maxN = max(maxN, arr[i])
        return result[::-1]
s = Solution()
print s.leader([16, 17, 4, 3, 5, 2])
