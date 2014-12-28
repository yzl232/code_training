# encoding=utf-8
'''
Given a 'friendship' graph, how would you generate friend suggestions for people, and how would you distribute the data across machines?
'''

'''
To generate friend suggestions, for a person in the graph find all the friends connected to this person(1-HOP) then suggest the friends of these friends(2-HOP).
We can refine this more by suggesting 2-HOP friends who have common attributes like same school, same subject of interest, etc.. so on to order the suggested friends list.

I guess it would be better to store connected nodes(friends) in the graph on the same server machine since there is a high chance that friends will want to see updates from friends. Though some nodes on the friends graph will be redundant on more than one machine.
'''