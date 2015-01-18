# encoding=utf-8
'''
In gmail, while composing an email, upon adding a contact, related contacts are displayed. How would you implement that feature?

- Write an algorithm for that.

- What data structure would you use to store the weights?

- In what format would you persist this data?
'''
#我的想法。   每个用户class存了一个related.  存在了hashtable。    或者heap

'''
I think the simplies solution for this is a dictionary of dictionaries. We need to quickly find relations for a given key (email), so dictionary with key by email. We might have selveral relations and we need to store weight for each of them, so another dictionary.
'''

# we can use sparse matrix to contain the data.