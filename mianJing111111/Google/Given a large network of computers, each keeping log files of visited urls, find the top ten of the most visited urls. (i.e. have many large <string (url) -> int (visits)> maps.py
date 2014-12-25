# encoding=utf-8
'''
Given a large network of computers, each keeping log files of visited urls, find the top ten of the most visited urls.
(i.e. have many large <string (url) -> int (visits)> maps, calculate implicitly <string (url) -> int (sum of visits among all distributed maps), and get the top ten in the combined map)

The result list must be exact, and the maps are too large to transmit over the network (especially sending all of them to a central server or using MapReduce directly, is not allowed)
'''

#hash  mod的方法。
'''
Denote N as the number of computers in our network.

1) Pick a good string hash function. This function must take urls as input and produce hash values uniformly in the range [0, MAX_HASH_VALUE]

2) Divide the hash range [0, MAX_HASH_VALUE] into N intervals with equal length MAX_HASH_VALUE / N, and assign each interval to 1 computer in the network, e.g.
CPU_1) [0, length-1]
CPU_2) [length, 2*length-1]
CPU_3) [2*length, 3*length-1]
...
CPU_N) [(N-1)*length, MAX_HASH_VALUE]

3) Each computer computes the hash values of its list of urls and sends the url and its visited information to the computer responsible by the hash of that url.

4) Each computer received a list of information url->visits for the urls in its hash interval. Now it must combine the visits of the urls and produce its top 10.

5) Each computer sends its top 10 to a central computer. This central computer will receive 10*N urls and compute the overall top 10.

Due to our good hash function, we expect that each computer will receive roughly the same amount of urls to process in the 4th step. I think this approach is the best we can do to distribute the work among the cluster.

About the constraints, they're not very clear.
a) This is sending all urls over the network but not to a single computer. In order to produce an exact result, I think all approaches end up sending all urls over the network in the worst case. Again, we would need to discuss with the interviewer if this is ok (the "especially sending all of them to a central server" part).

b) This is similar to MapReduce. I think that by saying "using MapReduce directly is not allowed", the interviewer meant that we have to give a detailed explanation about how the work is distributed among the network of computers, instead of just saying "the MapReduce framework will distribute and combine the work for us".
'''