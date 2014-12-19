# encoding=utf-8
'''
given 10 files (text files) each of size of 900 Mb. givena another file named "hello". match the contents of this file with other 10 file and return the file whose contents closely match with the contents of file "hello"
'''

'''
Score each file's contents on several parameters:
1) no. of words
2) no. of letters
3) no. of spaces
4) count of each of the letters  #hashmap
5) count of each words   #hashmap
etc

Give weightage to each of the properties and arrive at a number (score). The closest of the scores is the answer.
'''