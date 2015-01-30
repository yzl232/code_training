# encoding=utf-8
'''
not algorithm: get random from distributed system, no duplication
'''

#Number of machines.
# randint(1, N)
# random from the machine
# 前提是要每个machcine等价。


#目的是概率相等。  我们可以划分区域。 比如一共。 3000个数。  一号machine1000个数 。 二号2000个数。
# 如果x= randomint(1, 3000)  if x<1000. 一号machine.