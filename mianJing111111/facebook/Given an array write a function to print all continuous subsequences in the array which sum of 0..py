# encoding=utf-8
'''
Given an array write a function to print all continuous subsequences in the array which sum of 0.
e.g:
Input:
Array = [-1, -3, 4, 5, 4]
output:
-1, -3, 4

暴力法。 寻找所有start, end。  O(n2)

O(n)



1) run cumulate sum on the original array
2) append [0] in font of this cum_sum_array
3) check if two item in this cum_sum_array are same (for requirement sum==0, this could be done in O(n))



# 最极端的最坏情况还是 O(n2)
平均来说是O(n)

很巧妙


关于subsequence  如果是说 continuous。 那就是正常的subarray。 否则就是按顺序的subsequence


之前的和，也就是左边的和
'''


def get_sum(array):
    cumuSum = array[:]
    for i in range(1, len(cumuSum)):
        cumuSum[i] = cumuSum[i-1]+array[i]
    cumuSum = [0]+ cumuSum
    results = []
    d = {}
    for index in range(len(cumuSum)):
        s = cumuSum[index]
        if s not in d:
            d[s] = [index]
        else:    # found valid subsequences
            for start in d[s]:
                results.append(array[start:index])
            d[s].append(index)
    print cumuSum
    return results