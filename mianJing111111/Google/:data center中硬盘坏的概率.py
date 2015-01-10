# encoding=utf-8
'''
上来一大堆介绍，迷惑我的，我精简一下问题:data center中硬盘坏的概率是1/100000
，现在每一个硬盘都有一个检测程序，但是它只有99%的正确率，意思就是，100个里面
它可能有一个判断错误，好的认为是坏的，坏的认为是好的。Please analyze the
impact of this diagnostic program。我晕菜了，他的意思其实是好的硬盘被误诊的
概率非常高，就是说1%远比1/100000小
'''


'''
The probability of broken harddrive is 0.001%
The probability of correct detection is 99%


indicating the probability of missed detection is 0.001% * 1%~=0.00001%

while the probability of false alarm is 99.999%*(1-99%)~=1%

The overall accuracy is true intact + true broken/all cases is no doubt-able
99%, ROC is pretty good already.
'''