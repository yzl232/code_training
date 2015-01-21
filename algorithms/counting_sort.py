# encoding=utf-8
def countingSort(array, maxVal):
    m = maxVal + 1
    cnt = [0]*m; ret=[]
    for a in array: cnt[a]+=1
    for i in range(len(cnt)):
        ret+=[i]*cnt[i]
    return ret

print countingSort( [1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1], 7 )