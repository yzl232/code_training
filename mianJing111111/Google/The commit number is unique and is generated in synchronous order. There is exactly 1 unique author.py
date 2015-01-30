# encoding=utf-8
'''
The commit number is unique and is generated in synchronous order. There is exactly 1 unique author


The setup is that we are given a series of text files which contain information regarding a code repository's commits. Each file represents a single commit and they are formatted as follows:
"
Commit #: XXX
Author: XXX
Reviewer(s): XXX, XXX, ...
File: XXX
File: XXX
...
Date: XX:XX:XX XX/XX/XXXX
"
The commit number is unique and is generated in synchronous order. There is exactly 1 unique author. There are a variable number of reviewers, delimited by commas; if there are no reviewers, that line is absent from the file. There are a variable number of edited files in the commit, each receiving its own line. The time/date is when the commit was submitted.


First design a graphical model for all of the commit data. Then describe how this model is updated when a new commit is generated. Finally, write the code segment called when a new commit is generated which edits a system that has implemented your model of the data - its input is a file name and whatever necessary data structures that are maintained by your system.
'''



'''
First, the question is not that clear, what does the interviewer want to see. But it seems that it requires to design a System like Git.
Second, the solution is like:

#主要就是file,  commit两个量。  有点像bipartie的图。

#array of commits.  时间排序    以及相关的pointer to files
# file 是一个hashtable。  存了相关的commits.

1) Keep a list of managed files (say, L) and their status.
2) Each file has a connection to all related commits. (commits are ranked based on time)
3) Each commit has a connection to all related file (including not-changed files).

For the latest version, scan the files and fetch the latest files.
For one particular commit, scan the related files and fetch the files.

Each time, when a new commit happens,
1) If the commit new a file, insert the file to L.
2) For all modified files, insert the commit into the beginning.
3) Insert the commit to the ranked commit list.
'''