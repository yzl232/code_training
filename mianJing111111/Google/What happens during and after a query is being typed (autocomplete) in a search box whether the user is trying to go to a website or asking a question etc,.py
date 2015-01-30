# encoding=utf-8
'''
What happens during and after a query is being typed (autocomplete) in a search box whether the user is trying to go to a website or asking a question etc, and how do servers complete the request and what is the best (parallel) structure for the request to go through. DFS and how servers are located for proximity
'''

'''
Lets take example of Google page - auto suggestion. This is what I believe should be happening.
1. When user enters into search box, the view module (ex jsp) makes a call the google webapp servlet with user inputs as parameter string using ofcourse AJAX.  (把query传给server)
2. Based on the inputs / paramter string the server looks up the possible suggestion by looking up the data structure that stores all the previous searched strings. Data structure here would best be Trie. search is a DFS  (server在trie里边找prefix. DFS。  并且应当也有hash统计了次数。  top10)
3. after completing all strings search, the servlet sends back the collection to view module.
4. view on reciept of response, sets the respective DOM object to display the suggestion.

This happens as you type :).
'''

class Solution:
    pass