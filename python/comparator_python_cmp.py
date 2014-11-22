# encoding=utf-8
def my_cmp(E1, E2):
    return 0-cmp(E1[1], E2[1])    #compare weight of each 2-tuple
                    #return the negative result of built-in cmp function
                    #thus we get the descend order
L = [('a', 0), ('b', 1), ('c', 2), ('d', 3)]
L.sort(my_cmp)   #注意，传入的只是函数名
print L



arr = [ [1, 7],  [3, 2] ]
def sqSum(a):
    return a[0]*a[0]+a[1]*a[1]

def myCMP(a, b):
    if sqSum(a)>sqSum(b): return 1
    elif sqSum(a)<sqSum(b): return -1
    return 0

arr.sort(myCMP)  #注意，传入的知识函数名
print arr

