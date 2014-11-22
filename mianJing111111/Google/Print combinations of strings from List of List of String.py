# encoding=utf-8
'''
Print combinations of strings from List of List of String

Print combinations of strings from List of List of String

Example input: [[quick, slow], [brown, red], [fox, dog]]

Output:
quick brown fox
quick brown dog
quick red fox
quick red dog
slow brown fox
slow brown dog
slow red fox
slow red dog
'''



input_list = [['quick', 'slow'], ['brown', 'red'], ['fox', 'dog']]
class Solution:
    def printCombinations(self, inputList):
        self.result = []
        self.combinations('', input_list)
        for i in self.result:
            print i

    def combinations(self, tmpResult, input):
        if not input:
            self.result.append(tmpResult[1:])
            return
        items = input[0]
        for item in items:
            self.combinations(tmpResult + ' ' + item, input[1:])

s = Solution()
print s.printCombinations(input_list)