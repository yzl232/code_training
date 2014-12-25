# encoding=utf-8
'''
How does a search engine perform exact phrase search? i.e. search for the term "the bees knees" exactly.
'''

#http://en.wikipedia.org/wiki/Inverted_index

'''
When a phrase search is done, there could be multiple ways based on how the search engine is implemented. Will explain one way here.
Each of the words of the phrases are searched on the inverted index and the posting lists of the corresponding words will all be retrieved. We can do a repeated intersection of the sets of documents in the posting lists..
In the document set where all the words are present, a more detailed search for the specific location of the word in the documents where each of these words occur. The result will have those documents that have them in the consecutive positions in each of the documents in the specified order.
Sometimes the phrases may be stored as they are too.. For instance to search phrases like "To be or not to be", which consists of all stopwords..
If the n gram frequencies in words or phrases are stored as in vector space models, phrase searches are simpler.
'''