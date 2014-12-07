# encoding=utf-8
'''


Two very large numbers are represented using arrays. Multiply these two numbers. E.g. Two numbers 12 and 13 are represented as a=[1,2] adn b=[1,3]. The expected result is 12*13=156 i.e. c=[1,5,6]


leetcode原题

'''
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        num1, num2 = num1[::-1], num2[::-1]
        result = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i + j] += int(num1[i]) * int(num2[j])
        carry, total = 0, []
        for digit in result:
            sum = carry + digit
            carry = sum / 10
            total.append(str(sum%10)) #也append的反面  total.insert(0, str(sum % 10))
        while len(total) > 1 and total[-1] == "0": total.pop()
        return ''.join(total[::-1])