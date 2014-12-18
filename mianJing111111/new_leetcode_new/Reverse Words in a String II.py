# encoding=utf-8
'''
Reverse Words in a String II

given s = "the sky is blue", return "blue is sky the".

Similar to Question [6. Reverse Words in a String], but with the following constraints:
“The input string does not contain leading or trailing spaces and the words are always separated by a single space.”
Could you do it in-place without allocating extra space?


This can be done without any additional space in 2 pass
1) reverse the string in place
2) reverse each word of the reversed string.

'''

#变化比较多。 都要熟练掌握。 多练习

'''
第一轮coding，很简单的leetcode原题就是翻转单词那道，之前感觉那题很简单都没多想。。上来用split做结果面试官说这样要来回复制用了很多空间，我当时状态不好也没想到别的，他就让我先写了这个，然后各种test case测试，改bug，之后一步步减少中间不必要的临时空间，直到最后他说让我no extra space，我说你给我一个string怎么可能no extra space啊，他说你可以用其他数据结构表示string啊。。我靠这也行。。最后用char array的方法又写了一遍，我们一起想了差不多8个test case其中有各种bug，他一遍遍让我改。面完这轮心情非常糟糕啊，因为看面经都要快速写bug free才行的，我问了他下我是不太水了啊，一轮就做了个简单题，他说我考这道题好几次了，一般要不就直接写了最好的那种，要不就写了split那种，两种都写很少的，所以你这个挺好的。
'''
# he is nice
# eh si ecin
# nice is he

class Solution:#input is a char array.
    def reverseWords(self, arr):     #in place
        i=0
        for j in range(len(arr)+1):
            if j==len(arr) or arr[j] == ' ':  #结尾
                self.reverse(arr, i, j-1)
                i = j+1 #更新start
        self.reverse(arr, 0, len(arr)-1)  #逐个reverse。最后整体reverse
        return arr

    def reverse(self, arr, i, j):
        while i<j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1;  j-=1

s = Solution()
print s.reverseWords(list('the sky is blue'))

#自己实现split.  #只有一个space的情况
class Solution:  #O(n) space
    def reverseWords(self, s):
        ret = '';   j = len(s)
        for i in range(len(s)-1, -1, -1):
            if i==0 or s[i-1]==' ':  #单词的开始.  找到空格。 更新end。更新单词
                ret+=s[i:j]+' '
                j=i-1
        return ret[:-1] if ret else ''
s = "the sky is blue"
s1 = Solution()
print s1.reverseWords(s)



#和上面不同。 这个是多个space的情况。 以及边界space的情况
class Solution:  #O(n) space
    def reverseWords(self, s):
        ret = '';   j = len(s)
        for i in range(len(s)-1, -1, -1):
            if s[i]==' ': j=i   #找到了一个可能的结尾
            elif i==0 or s[i-1]==' ':      ret+=s[i:j]+' '   #单词的开始.  意思是现在不是空格。 i-1是空格。 必须加上.  非空格才更新
        return ret[:-1] if ret else ''
s = "the sky is    blue    "
s2 = Solution()
print s2.reverseWords(s)