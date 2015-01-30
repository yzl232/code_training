# encoding=utf-8
#对于一个totally random的array，长度为n，这个min平均会被reassign多少次
'''
说是给一个array让你求minimum的话，肯定是弄一个min = max integer，然后一路碰到更小的就reassign这个值，最后返回这个值就是minimum。现在问题来了…

，对于一个totally random的array，长度为n，这个min平均会被reassign多少次。
'''

#想象一个无限长的线段被平均分成2段， 4段， 5段。。。


# 解释。  就是random来说，
#http://stackoverflow.com/questions/6735701/number-of-assignments-necessary-to-find-the-minimum-value-in-an-array

'''

The chance that the second number is larger than the first is 1/2. Regardless of that, the chance that the 3rd number is larger than two before, is 1/3. These are all independent chances and the total expectation is therefore

1/2 + 1/3 + 1/4 + .. + 1/n
'''

#对于本题。 则是1/1+1/2 + 1/3 + 1/4 + .. + 1/n


