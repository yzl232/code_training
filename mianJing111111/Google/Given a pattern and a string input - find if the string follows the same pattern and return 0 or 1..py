# encoding=utf-8
'''
 Given a pattern and a string input - find if the string follows the same pattern and return 0 or 1.
Examples:
1) Pattern : "abba", input: "redbluebluered" should return 1.
2) Pattern: "aaaa", input: "asdasdasdasd" should return 1.
3) Pattern: "aabb", input: "xyzabcxzyabc" should return 0.
'''


'''
say pattern is abbab [2 a's and 3 b's] and string = redblueblueredblue [18 chars]
Let number of chars in 'a' = x and 'b' = y

2x + 3y = 18
find all possibilities of x and y,
here it came : x = 3 and y = 4

Loop over all possibilities of x and y
'''

#一个小优化： 因为3 > 2  所以for y in range(6):