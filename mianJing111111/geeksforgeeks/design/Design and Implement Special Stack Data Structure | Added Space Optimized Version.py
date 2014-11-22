# encoding=utf-8
'''
Question: Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack. All these operations of SpecialStack must be O(1). To implement SpecialStack, you should only use standard Stack data structure and no other data structure like arrays, list, .. etc.

Example:

Consider the following SpecialStack
16  --> TOP
15
29
19
18

When getMin() is called it should return 15, which is the minimum
element in the current stack.

If we do pop two times on stack, the stack becomes
29  --> TOP
19
18

When getMin() is called, it should return 18 which is the minimum
in the current stack.



Solution:
 Use two stacks: one to store actual stack elements and other as an auxiliary stack to store minimum values.

 The idea is to do push() and pop() operations in such a way that the top of auxiliary stack is always the minimum.
 Let us see how push() and pop() operations work.

Push(int x) // inserts an element x to Special Stack
1) push x to the first stack (the stack with actual elements)
2) compare x with the top element of the second stack (the auxiliary stack). Let the top element be y.
…..a) If x is smaller than y then push x to the auxiliary stack.
…..b) If x is greater than y then push y to the auxiliary stack.

int Pop() // removes an element from Special Stack and return the removed element
1) pop the top element from the auxiliary stack.
2) pop the top element from the actual stack and return it.

The step 1 is necessary to make sure that the auxiliary stack is also updated for future operations.

int getMin() // returns the minimum element from Special Stack
1) Return the top element of auxiliary stack.

We can see that all above operations are O(1).
Let us see an example. Let us assume that both stacks are initially empty and 18, 19, 29, 15 and 16 are inserted to the SpecialStack.
'''
class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        if len(self.stack)==0:
            self.stack.append(x)
            self.minStack.append(x)
        else:
            self.stack.append(x)
            tmp = self.minStack[-1]
            self.minStack.append(min(x, tmp))
    # @return nothing

    def pop(self):
        tmp = self.stack.pop()
        self.minStack.pop()
        return tmp

    # @return an integer
    def top(self):
        if len(self.stack)>0: return   self.stack[-1]


    # @return an integer
    def getMin(self):
        if len(self.stack)==0: return
        return self.minStack[-1]