# encoding=utf-8
'''
Hailstone Value
Hailstone 数列，从一个数n开始，如果n是奇数 乘3 +1， 如果是偶数就除以2， 直到到1为止（虽然没有人可以证实，但所有的数都可以到1）
给你一个positive int， 找到经过多少步可以到1，定义为hailstone value
比如， 2 -- 1， 输出是1  ； 3 -- 10 -- 5 -- 16 -- 8 -- 4 -- 2 -- 1，输出是7

2.
给你一个n，打印所有从1-n中 number whose hailstone value isgreater than that for any smaller number.. 1point 3acres 璁哄潧
比如n = 6
1 -- 0
2 -- 1
3 -- 7
4 -- 2（这里2< 7, 4不可以打印）
5 -- 5 （5 < 7, 不打印）
6 -- 8
调用了1的function，不难


3. 如何降低复杂度
其实就是有很多重复计算的问题，我觉得主要是提高1这个function，用了hashmap

其实后来跟同学讨论了一下，可能可以从序列末尾开始，因为只要我们可以算到2的n次方，那么剩下的操作就都是除2. W
'''

def hailStone(n):
	cnt=0;	skip=set([]);  orig=n
	while n>1:
		if n%2==0:	n/=2
		else: 	n=n*3+1
		if n>orig:	skip.add(n)    #碰到更大的数， 肯定不满足条件 。  (cnt会更小)
		cnt+=1
	return cnt,skip



def allHail(n):
	skipS={}
	res=[]
	for i in range(1,n+1):
		if i in skipS:	continue
		count,skip=hailStone(i)
		res.append((i,count))
		skipS.update(skip)   #省略重复运算。
	return res

print allHail(6)