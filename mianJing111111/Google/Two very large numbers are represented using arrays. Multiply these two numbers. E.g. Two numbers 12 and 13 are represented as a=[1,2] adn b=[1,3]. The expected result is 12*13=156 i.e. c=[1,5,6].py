# encoding=utf-8
'''


Two very large numbers are represented using arrays. Multiply these two numbers. E.g. Two numbers 12 and 13 are represented as a=[1,2] adn b=[1,3]. The expected result is 12*13=156 i.e. c=[1,5,6]

Normal Multiplication:

      563
   *  842
---------------
      1126
     2252
    4504
----------------
    474046
----------------

'''
class Solution:
    def multiplyTwoNumber(self, a, b):
        c = [0 for i in range(len(a)+len(b))]  #极端情况。 999**2 = 998001
        s = len(c)-1
        for j in range(len(b)-1, -1, -1):  #从右往左。
            carry = 0
            shift =s   # s 也是代表最右边的位数。  每次shift从右往左
            for i in range(len(a)-1, -1, -1):
                m = a[i] * b[j]
                s_um = m + c[shift] + carry  #c[shift]是之前计算的和
                num = s_um%10   #
                carry= s_um/10
                c[shift] = num
                shift-=1
            c[shift] = c[shift]+carry  #没进位就是len(a),  有进位就是len(a)+1
            print c
            s-=1
        return c
s = Solution()
print s.multiplyTwoNumber([5, 6, 3],  [8, 4, 2])



#leetcode
class Solution678:
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
            total.insert(0, str(sum % 10))
        while len(total) > 1 and total[0] == "0":
            del total[0]
        return ''.join(total)