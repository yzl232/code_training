# encoding=utf-8
'''
Write a class DominoChecker that has a method called addBox(int[]) that takes a box of five dominoes, described as a list of 10 integers (explained after), adds it to a collection, and returns true if a box with the same dominoes was already in the collection and false otherwise. A box of dominoes is encoded as a list of 10 integers from 0 to 9, where a pair of numbers represent a domino. For example: 0,2,9,1,3,3,7,4,5,6 represents a box containing dominoes: (0,2); (9,1); (3,3); (7,4); (5,6). http://en.wikipedia.org/wiki/Dominoes for more basic info (like pictures)
'''

'''
Note that we're given 10 integers, each from 0 to 9. If we concatenate the 10 numbers we'll get at most 9,999,999,999 which fits in a 64 bit integer.
Also note that having dominoes (0,2) and (2,0) is the same, as having boxes [(0,2); (9,1); (3,3); (7,4); (5,6)] or [(0,2); (3,3); (5,6); (7,4); (9,1)] is also the same, the order does not matter.
'''

class DominoChecker:
    def __init__(self):
        self.d = {}

    def addBox(self, arr):
        for i in range(len(arr)):
            arr[i].sort()
        arr.sort()
        key =tuple(arr)  #或者改成string来hash
        if key in self.d: return False
        self.d[key]=1
        return True

    pass