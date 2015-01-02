# encoding=utf-8
'''
题：假设咱俩去抢银行，银行保险柜的锁是0到9、4位的密码锁。你在电话另一边给我念密码，我就一个一个试。假设你有一个string，所有的密码组合都是这个string的substring，问这个string的最小长度是多少。
如果不循环的话，长度为10003的序列是肯定存在的。这个叫debrujin sequence，有兴趣的同学可以研究下。
后来问怎么求，我说图，然后哈密瓜路径，DFS
'''

#https://www.youtube.com/watch?v=iPLQgXUiU14
# Hamilton Cycle,  Euler Cycle
#暴力
# 高端算法看不懂。 可以用brute force

'''
What is the shortest string that contains all the numbers from 0000 to 9999.

For example: '012345678' contains 0123, 1234, 2345, 3456, 4567, 5678.


'''
#理论上的最优长度是N+3=10003.   考虑循环cyclic，那就是10000

#暴力backtracking
class Solution:
    def de_bruijn(self):
        self.ret = list('0000');  self.visited = set(['0000'])
        if self.dfs():  return self.ret

    def dfs(self):
        if len(self.ret)==10003: return True
        for ch in '0123456789':
            cur = ''.join(self.ret[-3:]+ch)
            if cur in self.visited: continue
            self.ret.append(ch);   self.visited.add(cur)
            if self.dfs(): return True
            self.ret.pop();    self.visited.remove(cur)
        return False

#暴力法




class Solution:
    def de_bruijn(self, n=4, k=10):
        self.n = n;  self.k = k; self.seq = []
        self.dfs(1, 1, [0]*(n+1))
        return self.seq

    def dfs(self, t, p,cur):
        if t > self.n:
            if self.n % p == 0:   #
                self.seq+=cur[1:p+1]
        else:
            cur[t] = cur[t-p]
            self.dfs(t+1, p, cur)
            for j in range(cur[t-p]+1, self.k):
                cur[t] = j
                self.dfs(t+1, t, cur)

s = Solution()
ret = s.de_bruijn()
print ret, len(ret)

'''
http://en.wikipedia.org/wiki/De_Bruijn_sequence#Uses

The sequence can be used to shorten a brute-force attack on a PIN-like code lock that does not have an "enter" key and accepts the last n digits entered. For example, a digital door lock with a 4-digit code would have B(10, 4) solutions, with length 10,000. Therefore, only at most 10,000 + 3 = 10,003 (as the solutions are cyclic) presses are needed to open the lock. Trying all codes separately would require 4 × 10,000 = 40,000 presses.
'''




'''
4位的密码，遍历完所有0000-9999的可能性后，锁就能打开。

把所有的可能密码连接在一起成为总长度为4*10000=40000的string。这个string的某
连续四位肯定能够能解开锁。

上面的string不是唯一的。比如实际密码是2345，string的某5位是12345，1234是一个
组合，2345是另一个组合。也就是说他们共享了一些数字。导致总长度降低。

现在求一个最短的string，其中某连续4位一定是可以解开锁的密码。

'''


'''
一个密码锁四位，可以用一个长string,来每四个
每四个读来试密码，怎么设计这个长string用尽可能少的digits来试出0000-9999这一
万种可能。Hamilton回路问题，NP, dfs+recursion，Wikipedia上有代码。但是也有别
的方法。
'''



'''
密码锁问题，实现最短密码问题，版上有讨论。
这个题可以这么描述：
    一个数字串有4个数字，每个数字是 0 ~9 这10个数字。
    那么一共有0000 ~ 9999 共10,000个串。
    要求：找出一个最短的串，包含这10，000个数字串
'''


#出现过2道题目



#密码锁问题，实现最短密码问题，版上有讨论。

'''
For the "password" lock problem, the best solution is to use graph;

each number is a node, the directed edges between 2 nodes indicate extra
cost
if the dest comes after the source

for example "0000" to "0001" will be 1 while "0001" to "0000" is 4

Then problem becomes a hamilton path (np essentially)
'''



'''
码锁问题我要是在 G 家 onsite 前看过你的帖子就好了，
当时就想着找数学规律，没有想过用这种 “brute force”.

以下是我回来后写出的代码:
    bool DFS(vector<bool> & IsVisited, vector<char> & Result, int CurrNum){
        if(Result.size() == 10003) return true;
        int pre = (CurrNum % 10000) * 10;
        for(int i = 0; i < 9; ++i){
            int NextNum = pre + i;
            if(IsVisited[NextNum] == true) continue;
            Result.push_back('0'+i);
            IsVisited[NextNum] = true;
            if(DFS(IsVisited,Result,NextNum)) return true;
            Result.pop_back();
            IsVisited[NextNum] = false;
        }
        return false;
    }
    // initialize
    vector<bool> IsVisited(10000,false);
    vector<char> Result(4,'0');
    DFS(IsVisited,Result,0);
'''


'''
You can solve by finding an Eulerian tour.  Each node is a 3-digit number eg
100, and two nodes 100 and 001 are adjacent if they can be combined into
1001.  Now every node has equal in-degree and out-degree, thus an Eulerien
tour exists and can be found using the standard algorithm.




3. 密码锁问题，实现最短密码问题，版上有讨论。
这个题可以这么描述：
    一个数字串有4个数字，每个数字是 0 ~9 这10个数字。
    那么一共有0000 ~ 9999 共10,000个串。
    要求：找出一个最短的串，包含这10，000个数字串

    // Assume memory is not an issue here.
    // It is easy to find a memory efficiency way
    string calculate() {
        // assume all the strings are in an array vector<string> input;
        string result;
        for(int i=0; i<input.size(0; ++i) {
            result = input[i];
            unordered_set<string> visited;
            bool succeed = DFS(visited, input[i], result);
            if(succeed)
                return result;
        }
        // Can not generate!
        return "";
    }

    bool DFS(unordered_set<string> &visited, const string &node, string &
result) {
        visited.insert(node);
        if(visited.size() == 10000)
            return true;
        string nodeseg = node.substr(1, 3);
        for(int i=0; i<10; ++i)  {
            char ch = '0' + i;
            string nextNode = nodeset;
            nextNode.push_back(ch);
            if(visited.find(nextNode) != visited.end()) {
                result.push_back(ch);
                bool bSucceed = DFS(visited, nextNode, result);
                if(bSucceed)
                    return true;
                result.pop_back();
            }
        }
        visited.erase(node);

        return false;
    }
'''