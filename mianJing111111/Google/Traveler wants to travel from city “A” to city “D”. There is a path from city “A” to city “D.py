# encoding=utf-8
'''
Traveler wants to travel from city “A” to city “D”.
There is a path from city “A” to city “D”.
Path consists of steps, i.e. travel from city “A” to city “B”.
Path is encoded as sequence of steps.
Sequence is in incorrect order.
Your task is to restore order of steps in the path.
Input (unordered sequence):
C -> D
A -> B
B -> C
Output (Correctly ordered list which represents path):
A, B, C, D

Implement following API:

class Step {
String start;
String finish;
};

class Node {
String value;
Node next;
}

List<String> findPath(List<Step> steps) {
}
'''

#基本上是二元有向环的问题。  就是变成了==self.end就return而已

class Solution:
    def findCycle(self, arr, start, end):
        arr.sort(); self.end = end; self.start = start
        self.results = []
        self.d = {}
        for edge in arr:
            if edge[0]==self.start:
                candidates = arr[:]
                arr.remove(edge)
                self.dfs(edge[:], candidates)
        return self.results

#[1, 2],  [2, 8],  [1,  8]
    def dfs(self, tmpPath, candidates):
        if  len(tmpPath)!=len(set(tmpPath)): return   #cycle
        if tmpPath[-1]==self.end:
            self.results.append(tmpPath)
            return
        for edge in candidates:
            if tmpPath[-1] == edge[0]:
                tmpCan= candidates[:]
                tmpCan.remove(edge)
                self.dfs(tmpPath+[edge[-1]], tmpCan)