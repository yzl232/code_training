# encoding=utf-8
'''
Suppose the sub-requests can be queued at each server, and the servers are running all the time. Discuss feasible on-line algorithms that can achieve sub-optimal solutions with N ~ 10000
'''

'''
Here interviewer is expecting you to ask different questions
1) Is those request are entirely different?
--> If yes, then you just need to do load balancing, Use weighted round robin

2) If those N request are any one of 'M' request where M << N
--> Then take advantage of cache contents. Use Locality Aware Request distribution

3) If you want to take care of faulty machines as well
--> Use Consistent hashing

So there is no definite answer, Interviewer is expecting questions from you in this case.
'''