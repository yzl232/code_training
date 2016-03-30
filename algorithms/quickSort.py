# encoding=utf-8
import random
  
L = [2, 3, 8, 4, 9, 5, 6, 5, 6, 10, 17, 11, 2]  
  
def quickSort(arr):
    if len(arr) <=1: return arr
    pivot = random.choice(arr)
    s = [i for i in arr if i < pivot]
    m = [ i for i in arr if i== pivot]
    b = [i for i in arr if i>pivot]
    return quickSort(s) + m + quickSort(b)

print quickSort(L)



#quick selection  O(n)
def quickSelect(a, k):  #才7行。 背下
    assert k<=len(a)
    pivot = random.choice(a)
    s = [i for i in a if i<pivot]
    m = [i for i in a if i==pivot]     #写一下O(1)的partition写法。 这种效率略低。
    b = [i for i in a if i>pivot]
    if len(s)< k<=len(s)+len(m):      return pivot
    elif k<=len(s):       return quickSelect(s, k)
    else:        return quickSelect(b, k-len(s)-len(m))




# 以下是in place quick sort.   就是相当于2sum的2 pointer版本。 比较简单. 完全可以看看


def quickSort(arr):
    _quickSort(arr, 0 ,len(arr)-1)
    return arr

def _quickSort(arr, start, end):
    if end>start:
        pivot, i, j = arr[random.randint(start, end)], start, end
        while i<j:
            while i<j and  arr[i]<=pivot: i+=1       #这个东西太经典了。 背下
            while i<j and  arr[j]>pivot: j-=1
            arr[i], arr[j] = arr[j], arr[i]
            i+=1;  j-=1
        _quickSort(arr, start, j)  #这个时候j在左边了
        _quickSort(arr, i, end)
print quickSort([1, 5,3, 1, 3, 2])