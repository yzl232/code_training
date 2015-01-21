# encoding=utf-8
'''

Find the smallest positive number missing from an unsorted array

You are given an unsorted array with both positive and negative elements. You have to find the smallest positive number missing from the array in O(n) time using constant extra space. You can modify the original array.

Examples

 Input:  {2, 3, 7, 6, 8, -1, -10, 15}
 Output: 1

 Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
 Output: 4

 Input: {1, 1, 0, -1, -2}
 Output: 2


geeks看到
leetcode 原题
'''

class Solution: #如果是所有数在0-n，那就用求和相减就可以做。  geeksforgeeks。 这里没有
    # @param A, a list of integers
    # @return an integer  # naive thought:  用hashtable. 然后从1到N看是否在hashtable中。 O(n) space and time
    def firstMissingPositive(self, a):
        n = len(a);  i=0   #理想的情况是1~n的组合.  (这句话是本题的关键)  1<=a[i]<=n   #小于0的忽略。
        while i<n:
            t = a[i]-1  #求index  -1
            if 0<=t<=n-1 and a[i] != a[t]:    #小于n+1.不然越界。 # 2种都不等于
                a[i], a[t] = a[t], a[i]   #不更新i #a[i]的元素搞定了。a[t]没搞定
            else: i+=1
        for i in range(n):
            if a[i] != i+1:     return i+1  #求值 +1
        return n+1
