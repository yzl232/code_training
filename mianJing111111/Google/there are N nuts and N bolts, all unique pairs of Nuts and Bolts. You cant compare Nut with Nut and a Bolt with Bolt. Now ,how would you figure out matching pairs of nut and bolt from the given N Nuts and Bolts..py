# encoding=utf-8
'''
there are N nuts and N bolts, all unique pairs of Nuts and Bolts. You cant compare Nut with Nut and a Bolt with Bolt. Now ,how would you figure out matching pairs of nut and bolt from the given N Nuts and Bolts.

'''

'''
方法就是类似快排，随便找一个螺母a，用它把所有螺栓分成小于a、大于a和等于a（只有一个）。再用那个等于a的螺栓把所有螺母也划分一遍。于是就得到了一对匹配和“大于a的螺母螺栓”、“小于a的螺母螺栓”两部分，递归处理。复杂度和随机选取pivot的快排的复杂度一样。
'''

#code很难写。 懒得写了。

#G家面经也有这道题目

# encoding=utf-8

'''

# encoding=utf-8
import random

class Solution:
    def partition(self, v, pv, start, end):
        p = v[start:end].index(pv) + start
        v[p], v[end-1] = v[end-1], v[p]   #pivot存到最后......
        evict_idx = i =start
        while i<end:
            if v[i] < pv:
                v[evict_idx], v[i] = v[i], v[evict_idx]
                evict_idx+=1
            i+=1
        v[evict_idx], v[end-1] = v[end-1], v[evict_idx]
        return evict_idx

    def qSort(self, bolts, nuts, start, end):
        if end-start>1:
            a_bolt = random.choice(bolts[start: end])
            a_nut_idx = self.partition(nuts, a_bolt, start, end)  #这是与标准的不同。 拷贝了2次
            a_nut = nuts[a_nut_idx]
            a_bolt_idx =self.partition(bolts, a_nut, start, end)
            self.qSort(bolts, nuts, start, a_bolt_idx)
            self.qSort(bolts, nuts, a_bolt_idx+1, end)

random.seed(1)

N = 10

b = [ random.randint(1,20) for _ in range(N) ]
n = b[:]
random.shuffle(n)

print("b = ", b)
print("n = ", n)
s = Solution()
s.qSort(b,n, 0, N)

print("b = ", b)
print("n = ", n)
'''

#我还是适合简单版本
import random

def quickSort(arr1, arr2):
    assert len(arr1)==len(arr2)
    if len(arr1) <=1: return arr1, arr2
    pivot = random.choice(arr1)
    s2, m2, b2 = partition(arr2, pivot)
    assert m2!=[]
    pivot = m2[0]
    s1, m1, b1 = partition(arr1, pivot)
    s1, s2 = quickSort(s1, s2)
    b1, b2 = quickSort(b1, b2)
    return s1+m1+b1, s2+m2+b2

def partition(arr, pivot):
    s = [i for i in arr if i < pivot]
    m = [ i for i in arr if i== pivot]
    b = [i for i in arr if i>pivot]
    return s, m, b


N = 10

b = [ random.randint(1,20) for _ in range(N) ]
n = b[:]
random.shuffle(n)
print b, n
print quickSort(b, n)