# encoding=utf-8
'''
输入一个整数,输出他的英文读法
1 -> one
100 -> one hundred
500234 -> five hundred thousand two hundred thirty four
1232232 -> 1 million two hundred .....
'''
#naive 方法就是1~99 全部存到hashmap。  这个是存了30个。 我觉得存99个没问题。

numToWords = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety"
}
def int_to_english(n):
    ret = []
    ones = n % 10;   tens = n % 100   #0~9,   11~99
    hundreds = (n / 100) % 10  #因为只考虑100到900  ， 1-9
    thousands = (n / 1000)
    if thousands:
        ret.append(int_to_english(thousands))
        ret.append('thousand')
        if not hundreds and tens: ret.append('and')    #可以省略     and就是在几十几前面加上去的。
    if hundreds:
        ret.append(numToWords[hundreds])
        ret.append('hundred')
        if tens: ret.append('and')
    if tens:  #如果存99个数字到hashmap。 这下面三行不需要了。
        if tens < 20 or ones == 0:    ret.append(numToWords[tens])
        else:
            ret.append(numToWords[tens - ones])
            ret.append(numToWords[ones])
    return ' '.join(ret)

print int_to_english(93256)

