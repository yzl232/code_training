# encoding=utf-8
def countingSort(array, maxVal):
    m = maxVal + 1
    cnt = [0]*m
    for a in array: cnt[a]+=1
    k=0
    for val in range(len(cnt)):
        for j in range(cnt[val]):
            array[k]=val
            k+=1
    return array