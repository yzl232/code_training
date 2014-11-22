# encoding=utf-8
'''


The Celebrity Problem

Another classical problem.

In a party of N people, only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. We can only ask questions like “does A know B? “. Find the stranger (celebrity) in minimum number of questions.

We can describe the problem input as an array of numbers/characters representing persons in the party. We also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B, false otherwise. How can we solve the problem, try yourself first.

We measure the complexity in terms of calls made to HaveAcquaintance().

Graph:

We can model the solution using graphs. Initialize indegree and outdegree of every vertex as 0. If A knows B, draw a directed edge from A to B, increase indegree of B and outdegree of A by 1. Construct all possible edges of the graph for every possible pair [i, j]. We have NC2 pairs. If celebrity is present in the party, we will have one sink node in the graph with outdegree of zero, and indegree of N-1. We can find the sink node in (N) time, but the overall complexity is O(N2) as we need to construct the graph first.

Recursion:

We can decompose the problem into combination of smaller instances. Say, if we know celebrity of N-1 persons, can we extend the solution to N? We have two possibilities, Celebrity(N-1) may know N, or N already knew Celebrity(N-1). In the former case, N will be celebrity if N doesn’t know anyone else. In the later case we need to check that Celebrity(N-1) doesn’t know N.

Solve the problem of smaller instance during divide step. On the way back, we may find a celebrity from the smaller instance. During combine stage, check whether the returned celebrity is known to everyone and he doesn’t know anyone. The recurrence of the recursive decomposition is,

T(N) = T(N-1) + O(N)

T(N) = O(N2). You may try Writing pseudo code to check your recursion skills.

Using Stack:

The graph construction takes O(N2) time, it is similar to brute force search. In case of recursion, we reduce the problem instance by not more than one, and also combine step may examine M-1 persons (M – instance size).

We have following observation based on elimination technique (Refer Polya’s How to Solve It book).

    If A knows B, then A can’t be celebrity. Discard A, and B may be celebrity.
    If A doesn’t know B, then B can’t be celebrity. Discard B, and A may be celebrity.
    Repeat above two steps till we left with only one person.
    Ensure the remained person is celebrity. (Why do we need this step?)

We can use stack to verity celebrity.

    Push all the celebrities into a stack.
    Pop off top two persons from the stack, discard one person based on return status of HaveAcquaintance(A, B).
    Push the remained person onto stack.
    Repeat step 2 and 3 until only one person remains in the stack.
    Check the remained person in stack doesn’t have acquaintance with anyone else.

We will discard N elements utmost (Why?). If the celebrity is present in the party, we will call HaveAcquaintance() 3(N-1) times. Here is code using stack.
'''