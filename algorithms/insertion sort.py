# encoding=utf-8
def sort_numbers(s):
    for i in range(1, len(s)):
        t = s[i]
        j = i - 1
        while j >= 0 and s[j] > t:   #j前面的都是sorted的
            s[j+1] = s[j]
            j = j - 1
        s[j+1] = t