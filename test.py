
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        dict.add(end)
        dict2 = dict.copy()
        wordLen = len(start)
        candidates1 = {start:1} ; candidates2 = {end:1}
        while True:
            if len(candidates1)==0:  break
            current1 = {};  current2=  {}
            for curWord  in candidates1:
                if curWord == end:return curLen
                for i in range(wordLen):
                    part1 = curWord[:i]; part2 = curWord[i+1:] # replace ith char
                    for j in 'abcdefghijklmnopqrstuvwxyz': # BFS
                        if curWord[i] !=j:
                            nextWord = part1 + j + part2
                            if nextWord in candidates2: return curLen+1+candidates2[nextWord]
                            if nextWord in dict:
                                current1[nextWord] =curLen + 1
                                dict.remove(nextWord)
            for curWord  in candidates2:
                curLen = candidates2[curWord]
                for i in range(wordLen):
                    part1 = curWord[:i]; part2 = curWord[i+1:] # replace ith char
                    for j in 'abcdefghijklmnopqrstuvwxyz': # BFS
                        if curWord[i] !=j:
                            nextWord = part1 + j + part2
                            if nextWord in candidates1: return curLen+1+candidates1[nextWord]
                            if nextWord in dict2:
                                current1[nextWord] =curLen + 1
                                dict2.remove(nextWord)
            candidates1 = current1
            candidates2 = current2
        return 0