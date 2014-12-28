# encoding=utf-8
'''
Design a web browser like Chrome with the tab functionality.
Also describe the data structure to be used.
'''

'''
Chrome stores everything in separate process, which implies that the parent process would keep a hashMap of all the process. The key would the index and value woud be the process. The process would provide the details with regard to tab-content. Movement of tabs is just swaping of hash-keys.

Each tab is a proces and have URL-Handler. The handler would call a factory of protocol, such as httpFactory, ftpFactory etc. Each protocol handler will call have a retrieving-engine and rendering-engine. The browser would retrieve and render using factory.
'''