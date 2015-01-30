# encoding=utf-8
#n boxes, k balls, expected number of empty boxes.
'''
比如If you have 10 balls and 5 boxes what is the expected number of boxes with no balls.



#期望  ：   取值xi与对应的概率Pi(=xi)之积的和称为该离散型随机变量的数学期望

x[i] 代表第几个盒子为空。的概率。

x = sum(x[i] for i in range(5) )

x[i] = 4**10/5**10       #  有一个box没有ball的概率

x = 5*   (4**10/5**10)  #


结果是 4**10/5**10  。

期望=x*prob(x)  =1* prob(1)

x = n*((n-1)**k)/(n)**k         #这个是概率吧~


'''
# http://math.stackexchange.com/questions/66077/how-to-find-the-expected-number-of-boxes-with-no-balls

'''
 类似的.
  Expected Number with $1$ Ball

x = sum(x[i] for i in range(5) )

x[i] =10*  ( 4**9/  5**10 )  #有某个盒子有一个球 的概率。

x = 5*  x[i] = 5*10* ( 4**9/  5**10 ) # 错误的。
 '''

# 分母总是种类。

#不完全正确。   x[0], x[1], x[2]可能会重叠。