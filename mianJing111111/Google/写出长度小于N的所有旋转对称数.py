# encoding=utf-8
'''

写出长度小于N的所有旋转对称数。
map['0'] = '0';
map['1'] = '1';

map['6'] = '9';
map['8'] = '8';
map['9'] = '6';



但是如果是数字时钟， 则要加上
map['2'] = '2';
map['5'] = '5';
'''
#如果只是判断一个数是不是，只要用ispalindrom加上map就可以做

# 看到G家考过2次

#  求长度小于N的中心对称的数字。中心对称的数字比如16891这种



'''
A valid number may not contain 2,3,4,5,7. Flip those numbers 180 degrees and
it's not a valid number. Single digit numbers is a special case. It
contains 0, 1, 8.



For 2N digit numbers, the first digit can be 1,6,8,9 and
the next N-1 digits can be 0,1,6,8,9. For 2N+1 digit numbers, you can insert
0,1,8 in the middle of any valid 2N digit numbers and it's still a valid
number.

1        digit: 3
2N     digit: 4 * 5 ^ (N-1)
2N+1 digit: 3 * 4 * 5 ^ (N-1)

'''
# 现生产N的部分。 对于2N, 2N+1可以此推出
#对于2N：只要处理前一半。后一半出来了
#对于2N+1:  就是2N中间插入0， 1， 8
# 因为这种递推关系， 每个位数有一个单独的array
class Solution:
    def solve(self, n):
        self.d ={'0':'0', '1':'1', '6':'9', '9':'6', '8':'8'}
        digitsN = len(str(n))
        ret = [[] for i in range(digitsN+1)]
        ret[1]=['0','1', '8']
        for i in range(2, digitsN, 2):    # 2N digits
            ret[i] = self.gen(i/2);
            ret[i+1] = [ x[:i/2]+ch+x[i/2:]  for ch in '018' for x in ret[i]]
        return ret

    def gen(self, n):
        self.nums = []
        for cur in '1689':    self.dfs(cur, n-1)
        return self.nums

    def dfs(self, cur, n):
        if n==0:
            self.nums.append(cur+''.join(self.d[ch] for ch in cur)[::-1])  #处理后半部分
            return
        for ch in '01689':     self.dfs(cur+ch, n-1)
s = Solution()
print s.solve(9999)
print s.solve(99999)



#valid    palindrome
class Solution:
    def palin(self, s):
        d ={'0':'0', '1':'1', '6':'9', '9':'6', '8':'8'}
        i=0; j=len(s)-1
        while i<=j:
            if s[i] not in d or s[j] not in d: return False
            if d[s[i]]!=s[j]: return False
            i+=1; j-=1