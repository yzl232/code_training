# encoding=utf-8
'''
和leetcode不一样。我傻了。。

Code a function that receives a string composed by words separated by spaces and returns a string where words appear in the same order but than the original string, but every word is inverted.
Example, for this input string

@"the boy ran"

the output would be

@"eht yob nar"

Tell the complexity of the solution.
'''
#这是leetcode的一部分
class Solution:#input is a char array.
    def reverseWords(self, arr):     #in place
        l=0
        for r in range(len(arr)+1):
            if r==len(arr) or arr[r] == ' ':  #结尾
                self.reverse(arr, l, r-1)
                l = r+1 #更新start
        return arr

    def reverse(self, arr, i, j):
        while i<j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1;  j-=1

s = Solution()
print s.reverseWords(list('the sky is blue'))


# leetcode in place 做法
class Solution:#input is a char array.
    def reverseWords(self, arr):     #in place
        l=0
        for r in range(len(arr)+1):
            if r==len(arr) or arr[r] == ' ':  #结尾
                self.reverse(arr, l, r-1)
                l = r+1 #更新start
        self.reverse(arr, 0, len(arr)-1)  #逐个reverse。最后整体reverse
        return arr

    def reverse(self, arr, i, j):
        while i<j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1;  j-=1
s = Solution()
print s.reverseWords(list('the sky is blue'))