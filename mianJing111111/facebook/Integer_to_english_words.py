# encoding=utf-8
'''
输入一个整数,输出他的英文读法
1 -> one
100 -> one hundred
500234 -> five hundred thousand two hundred thirty four
1232232 -> 1 million two hundred .....
'''
NUMBER_WORDS = {
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
    english_parts = []
    ones = n % 10
    tens = n % 100
    hundreds = (n / 100) % 10
    thousands = (n / 1000)

    if thousands:
        english_parts.append(int_to_english(thousands))
        english_parts.append('thousand')
        if not hundreds and tens: english_parts.append('and')    #可以省略
    if hundreds:
        english_parts.append(NUMBER_WORDS[hundreds])
        english_parts.append('hundred')
        if tens: english_parts.append('and')
    if tens:
        if tens < 20 or ones == 0:
            english_parts.append(NUMBER_WORDS[tens])
        else:
            english_parts.append(NUMBER_WORDS[tens - ones])
            english_parts.append(NUMBER_WORDS[ones])
    return ' '.join(english_parts)

print int_to_english(93256)