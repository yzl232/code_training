# encoding=utf-8
#输入为String类型的正整数，创建一个function做减1操作，比如: "123" - > "122", "100" - > "99"

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    # 100=>99     55=>54
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            digits[i]-=1
            if digits[i]>=0:   break
            digits[i]=9
        if digits[0]=='0' and digits!=[0]:return digits[1:]
        return digits