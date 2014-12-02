# encoding=utf-8
'''
iven an an unsorted array, sort the given array. You are allowed to do only following operation on array.

flip(arr, i): Reverse array from 0 to i

Unlike a traditional sorting algorithm, which attempts to sort with the fewest comparisons possible, the goal is to sort the sequence in as few reversals as possible.

The idea is to do something similar to Selection Sort. We one by one place maximum element at the end and reduce the size of current array by one.

最少的reverse


Following are the detailed steps. Let given array be arr[] and size of array be n.
1) Start from current size equal to n and reduce current size by one while it’s greater than 1. Let the current size be curr_size. Do following for every curr_size
……a) Find index of the maximum element in arr[0..curr_szie-1]. Let the index be ‘mi’
……b) Call flip(arr, mi)
……c) Call flip(arr, curr_size-1)
'''

#看看就行了

def flip(a,ArrayIndex):
    reverseList =[]
    for i in range(ArrayIndex,-1,-1):
        reverseList.append(a[i])
    for i in range(len(reverseList)):
        a[i] = reverseList[i]

def pancakeSorting(a):
    for i in range(len(a)-1, 0, -1):
        maxIndex = a.index(max(a[:i+1])) #找到最大
        if maxIndex==i: continue
        flip(a,maxIndex)  #最大放在第一个
        flip(a,i)  #最大在最后
    return a

def main():
    array= [45,7,3,89,123,56]
    print pancakeSorting(array)
if __name__ == '__main__':
    main()