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

#leetcode
class MinStack:
    # @param x, an integer
    def __init__(self):
        self.stack1 = [];  self.stack2 = []

    # @return an integer
    def push(self, x):
        self.stack1.append(x)  #小于或者等于。才push stack2
        if not self.stack2 or x <= self.stack2[-1]:   self.stack2.append(x)

    # @return nothing
    def pop(self):
        if self.stack1.pop() == self.stack2[-1]:    self.stack2.pop()  #cur与最小值相等。 pop stack2

    # @return an integer
    def top(self):
        return self.stack1[-1]

    # @return an integer
    def getMin(self):
        return self.stack2[-1]