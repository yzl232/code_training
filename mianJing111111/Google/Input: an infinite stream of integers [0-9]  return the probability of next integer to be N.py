# encoding=utf-8
'''
根据已有的频率判断新的概率
Input: an infinite stream of integers [0-9]
return the probability of next integer to be N

举例子，
input(1)
input(5)
input(0),
input(9)
input(0)
input(1)
then getProbability(n==0)=2/6
'''

#因为只有0~9
# cnt[0]~  cnt[9]
# totalCnt