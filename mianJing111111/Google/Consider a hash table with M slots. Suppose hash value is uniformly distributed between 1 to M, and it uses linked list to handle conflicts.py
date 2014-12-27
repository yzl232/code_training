# encoding=utf-8
'''
Consider a hash table with M slots. Suppose hash value is uniformly distributed between 1 to M, and it uses linked list to handle conflicts (if two keys hashed to the same slot). Suppose we put N keys into this M-slotted hash table, what is the probability that there will be a slot with i elements? i could vary from 0 to N.
'''

#我被考过。 应当是概率题目
#http://preshing.com/20110504/hash-collision-probabilities/
#上面的链接讲的马马虎虎
#排列组合
#  n的array,产生2个数

#概率题目都是A的总种类/ B的总种类。

'''
Calculating the Probability of a Hash Collision

 n的array,
产生1个数   p1  = 1- n/n
产生2个数   p2 =1-  n(n-1)/(n*n)
产生k个数   pk =1-   (n*(n-1)(n-2)...(n-k))


probability =1-  combinatin(n, k)/ (n**k)


'''


'''
暂时考虑的简单一点。 不考虑其他N-i个数
本题的解答:
probability = {M*（M-1）**  (N-i))   }/(M**N)
'''