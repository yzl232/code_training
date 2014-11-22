# encoding=utf-8
'''
Write a program which asks user to input numbers and find the smallest even number and largest odd number from those numbers
经过我的人工检验。 还是raw_inpu好用！！

'''
class Solution():
    def ask(self):
        smallEven =10**10; bigodd = -10**10
        nums = self.inputs()
        for i in nums:
            if i%2==0:   smallEven = min(smallEven, i)
            else:   bigodd = max(bigodd, i)
        return smallEven, bigodd

    def inputs(self):
        nums = [];  flag = True
        while flag:
            tmp = (raw_input("Enter a number: (enter 'stop' to stop ): "))
            if tmp=='stop': break
            nums.append(int(tmp))
        return nums
s = Solution()
print s.ask()