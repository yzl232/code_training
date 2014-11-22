# encoding=utf-8
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        numberToletter = {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        result = [""]
        for d in digits:
            result = [x+y for x in result for y in list(numberToletter[int(d)])]
        return result


s = Solution()
print s.letterCombinations('32')