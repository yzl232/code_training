# encoding=utf-8
'''
4 individual numbers which could be permuted in 4 factorial ways. permutation of these 4 integers is an 0indexedarray consisting of 4 digits in some order when integers are different. the best permute of the 4 integers is by the following funciton func(summ) = abs(summ[0] - summ[1]) + abs(summ[1] - summ[2] + abs(summ[2] - summ[3])) that would give maximum value.

method signature
public int answer(int w, int x, int y, int z){

}

w = 5
x = 3
y = -1
z = 5

the sample permute wiht given numbers in the given function that would give maximum value is as follows.

for the
summ[0] = 5
summ[1] = -1
summ[2] = 5
summ[3] = 3

'''
class Solution:
    def answer(self, w, x, y, z):
        val1=max(w, x, y, z)
        val2 = min(w, x, y, z)
        remain = [w, x, y, z]
        remain.remove(val1); remain.remove(val2)
        val3 = max(remain)
        val4 = min(remain)
        return (val1, val2, val3, val4)
'''
summ[0]=first maximum,
summ[1]=first minimum,
summ[2]=second maximum,
summ[3]=second minimum..
'''

#实际上才4个。暴力法才24种情况