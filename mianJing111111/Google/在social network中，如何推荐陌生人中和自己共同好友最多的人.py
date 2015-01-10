# encoding=utf-8
#在social network中，如何推荐陌生人中和自己共同好友最多的人


'''
Once common feature in Social Network site is to recommend people connection. e.g. "People you may know" from Linkedin. The basic idea is very simple; if person A and person B doesn't know each other but they have a lot of common friends, then the system should recommend person B to person A and vice versa.

From a graph theory perspective, for each person who is 2-degree reachable from person A, we count how many distinct paths (with 2 connecting edges) exist between this person and person A. Rank this list in terms the number of paths and show the top 10 persons that person A should connect with.

We should how we can use Map/Reduce to compute this top-10 connection list for every person. The problem can be stated as: For every person X, we determine a list of person X1, X2 ... X10 which is the top 10 persons that person X has common friends with.


'''


#如果用map reduce。 比较难。 不大看得懂。