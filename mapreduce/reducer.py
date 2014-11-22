__author__ = 'zhenglinyu'

from operator import itemgetter
import sys

word2count = {}
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\\t', 1)
    try:
        count = int(count)
    except:
        pass
