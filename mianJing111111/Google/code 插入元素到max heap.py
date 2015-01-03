# encoding=utf-8
# code 插入元素到max heap
#http://www.cs.cmu.edu/~adamchik/15-121/lectures/Binary%20Heaps/heaps.html
# http://www.algolist.net/Data_structures/Binary_heap/Insertion

#大概就是考察implement heap
class Heap:
    def __init__(self):
        self.size = 0
        self.arr = [None for i in range(4)]

    def insert(self, x):
        if self.size == len(self.arr):  self.arr +=[None for i in range(self.size)]  #乘以2
        p=self.size; self.size+=1
        while p and x>self.arr[p/2]:
            self.arr[p] = self.arr[p/2]  #大于parent， 就不断上移
            p/=2
        self.arr[p] = x