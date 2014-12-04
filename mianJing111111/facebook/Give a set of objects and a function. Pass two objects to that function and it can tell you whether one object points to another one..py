# encoding=utf-8
'''

Give a set of objects and a function. Pass two objects to that function and it can tell you whether one object points to another one. Find one object that is pointed by all other objects.

给你一个set<object> 然后给你了个compareTo的方法，可以比较出大小(任意两个objects都能比较出大小，但是这种关系不具有传递性，即 A>B,B>C但是A不一定大于C),让你找出set中最大的object，如果不存在，就返回null
'''

'''

乍一看感觉7，8题很相同，其实不然，第7题的A>B和B>A这两种关系是不能共同存在的，但是第8题 可以A喜欢B，B喜欢A，
第七题的解法，可以联想到擂台赛的解法，就是扫两次，第一扫的时候，找到其中最大的object，第二次扫的时候，让A可所以其它object比，如果还是比其它object大，那么它就是最大的，否则就是返回null
'''

#和celebrity problem解法一模一样，也有O(n)解法。 celebrity problem理解更加巧妙。

class Solution:
    def findCelebrity(self, objects):
        stack = objects[:]
        while len(stack)>1:  #eliminating stage
            u = stack.pop()
            v = stack.pop()
            if self.compareObjects(u, v):
                stack.append(v)
            else:   stack.append(u)
        if not self.verify(objects, stack[0]): return False   # no objects.
        return stack[0]

    def verify(self, objects, c):
        for p in objects:
            if not self.compareObjects(p, c): return False
        return True

    def compareObjects(self, o1, o2):
        pass