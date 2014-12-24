# encoding=utf-8
'''
Q: Design a component that will implement web browser history. the user goes to different site and once he press on history button you should display the last 5 (no duplicates allowed, and 5 can be any N later) if duplicates occur display the most recent one. so if user visit : G,A,B,C,A,Y and than press "history" we will display Y,A,C,B,G. and of course he can go later to two other websites and than press "history" we will show them than the previous 3.
'''

'''
This problem is the same as LRU cache design, using double linked list and hash table.
'''