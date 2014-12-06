# encoding=utf-8
def countingSort(array, maxVal):
    m = maxVal+1
    cnt = [0]*m
    for a in array: cnt[a] +=1  #用了一个辅助array  cnt
    i=0
    for a in array:
        for j in cnt[a]:
            array[i] = a
            i+=1
    return (array,count)

print countingSort( [1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1], 7 )