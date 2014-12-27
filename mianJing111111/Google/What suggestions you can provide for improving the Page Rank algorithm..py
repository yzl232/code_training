# encoding=utf-8
'''
What suggestions you can provide for improving the Page Rank algorithm.
'''
#随便看看。扯淡题目

'''
If the user is signed in , the algorithm can use the profile information of the user to return better search results , for example if the user regularly
searches about the computer science concepts, then algorithm can use this information to return results of the related field when there's an ambiguity in the search keywords , for example
if the user is searching for tree , the algorithm may assign more weights to the TREE datastructure.

If the user clicks on the k-th result the algorithm can reduce the relevancy of the the previous k-1 results.
If the user returns back to the search engine within a certain time frame and uses the same keywords it means that he/she is not satisfied with the past results , so the relevancy of the past results can be decreased.

The algorithm can also use soundex , stemming & translation algorithms to create larger number of results (this increases the False Positive).
The algorithm can also use the context of the keywords to guess what user is really looking for. (For this task, Natural Language Processing and Machine Learning Techniques may be useful)
'''