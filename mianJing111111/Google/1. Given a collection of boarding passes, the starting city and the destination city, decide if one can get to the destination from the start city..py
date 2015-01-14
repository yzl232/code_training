# encoding=utf-8
'''
Given a collection of boarding passes, the starting city and the destination city, decide if one can get to the destination from the start city.

   graph:
    MIA -> DC
    DC -> NYC
    DC-> MIA

    def can_reach(graph, MIA, NYC)


'''
#用一个BFS 。 加上visited考虑环吧。