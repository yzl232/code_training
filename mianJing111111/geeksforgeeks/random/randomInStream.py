# encoding=utf-8
'''
有一个流输入的文件，要求实时输出根据输入的等概率数字，比如输入1，输出1，输入12，输出1或者2（1和2各占50%），输入1112，输出1(75%概率)或者2(25%概率)。输入的数列是一直在实时输入的流，会非常大，不能离线记录。


Google有考这道题目。 面经
'''

import random
'''

看不大懂。 准备弃掉。
Select a random number from stream, with O(1) space

Given a stream of numbers, generate a random number from the stream. You are allowed to use only O(1) space and the input is in the form of stream, so can’t store the previously seen numbers.

So how do we generate a random number from the whole stream such that the probability of picking any number is 1/n. with O(1) extra space? This problem is a variation of Reservoir Sampling. Here the value of k is 1.

1) Initialize ‘count’ as 0, ‘count’ is used to store count of numbers seen so far in stream.
2) For each number ‘x’ from stream, do following
…..a) Increment ‘count’ by 1.
…..b) If count is 1, set result as x, and return result.
…..c) Generate a random number from 0 to ‘count-1′. Let the generated random number be i.
…..d) If i is equal to ‘count – 1′, update the result as x.


#像这种random的题目。一般来说，都是默认提供了数学的random()函数了



It's a google interview question with little variation.

Select a random quote from a given input file. Each quote can be of any no. of lines.

Ex input file:
Quote1 Line1
Quote1 Line2
Quote1 Line3
%%
Quote2 Line1
Quote2 Line2
Quote2 Line3
Quote2 Line4
Quote2 Line5
%%
Quote3 Line1
%%
Quote4 Line1
Quote4 Line2
Quote4 Line3
Quote4 Line4
%%
Quote5 Line1
Quote5 Line2
%%


'''

class Solution:

    def selectRandom(self, stream = [1, 4, 5, 13, 6, 7, 8]):
        cnt = 1; ret = stream[0]
        n =  len(stream)
        for i in range(n):
            x = stream[i]
            cnt += 1
            if random.randint(1, cnt)==1: ret = x
            print "Random number from first " +str(i+1)+" numbers is "+str(ret)

s = Solution()
print s.selectRandom()
'''
How does this work
We need to prove that every element is picked with 1/n probability where n is the number of items seen so far. For every new stream item x, we pick a random number from 0 to ‘count -1′, if the picked number is ‘count-1′, we replace the previous result with x.

To simplify proof, let us first consider the last element, the last element replaces the previously stored result with 1/n probability. So probability of getting last element as result is 1/n.

Let us now talk about second last element. When second last element processed first time, the probability that it replaced the previous result is 1/(n-1). The probability that previous result stays when nth item is considered is (n-1)/n. So probability that the second last element is picked in last iteration is [1/(n-1)] * [(n-1)/n] which is 1/n.
'''

