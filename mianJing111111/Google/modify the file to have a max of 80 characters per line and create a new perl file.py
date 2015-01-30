# encoding=utf-8
'''
Input : A Perl program file
We need to modify the file to have a max of 80 characters per line and create a new perl file.
Problem is we need to use "/" wherever we split the line and also, the split MUST happen at a place with white space. (ASSUMPTION - No is >75 characters)
'''
#分离的地方必须是white space的。。也就是word必须保留完整。而且'/'必须占用empty的位置
def split_line(content, MAX_LIMIT=80):
    ret=''
    while len(content) > MAX_LIMIT:
        words = content[:100].split(" ")
        cnt = 0
        for i in range(len(words)):
            cnt += len(words[i]) + 1
            if cnt > MAX_LIMIT:    break
        newline = " ".join(words[:i])
        content = content[len(newline):]
        if content:      ret+= newline + '/'
        else:  ret+= newline