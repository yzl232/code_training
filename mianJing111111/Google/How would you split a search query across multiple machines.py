# encoding=utf-8
#How would you split a search query across multiple machines
'''
Strategy of splitting a search query across multiple machines would depend on the type of distributed index maintained by the machines.

Typically for large scaled index, the architecture be, there will be set of master index servers 1 to n that index documents from the crawler. Index is maintained across all these servers.

For every index master server, there will be multiple (1 to m) slave servers with replicated indexes. These slave servers will handle queries.

Now typically a query analyzer will receive query fired from the browser. Query analyzer will split the query into multiple sub queries as follows:
So if the query is like "Google Mountain view jobs"
Sub queries:
1. complete query: "Google Mountain view jobs"
2. boolean query: "Google AND Mountain AND view AND jobs"
3. Distance / Proximity query: (Google Mountain) AND (Mountain view) AND (View jobs) AND (Google Mountain View) AND (Mountain View Jobs)
4 .Single word queries: Google, Mountain, view, Jobs

Typically there will be another fuzzy query analyzer which will re-issue single word queries as fuzzy queries
5. Single word fuzzy queries: Google~, Mountain~, view~, jobs~
6. Range Query: if the search term includes a date range, regular expressions will pickup the date range and create a date range query.

Once all the queries are finalized, the queries are fired across multiple shards (slave servers) in parallel.

Now this could be done using Publish Subscribe Messaging model or by directly firing query across multiple slave server using software or hardware load balanced way.

All the servers will receive one query each and will come up with the matching document result with the type weight (vector like structure) and count weight (no of word counts matched in the document).

Based on their individual weights, a dot product will be calculated to compute an IR score.Also a page rank score is calculated based on the search result page weight. (example: if the search resulted in wikipedia.org page then this result will have heigher value than mamapapa.com page which happens to have same searched terms)

Multiple results will be combined together based on their weight rank and page rank and first K results will be sent back to the server caching the complete result in the cache servers so that if the user clicks on page 2 of the result, the result can be sent back form the cache server than to compute the result all over again.
'''