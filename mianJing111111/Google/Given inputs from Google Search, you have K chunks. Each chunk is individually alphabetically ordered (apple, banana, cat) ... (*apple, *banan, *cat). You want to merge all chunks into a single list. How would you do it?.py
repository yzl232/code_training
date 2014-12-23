# encoding=utf-8
'''
Given inputs from Google Search, you have K chunks. Each chunk is individually alphabetically ordered (apple, banana, cat) ... (*apple, *banan, *cat). You want to merge all chunks into a single list. How would you do it?
'''

# min heap  size K

#We should create MinHeap containing first elements of chunk. Each time we extract min from the heap and push it to the output. And add new element from head of chunck, which element was pushed to output.