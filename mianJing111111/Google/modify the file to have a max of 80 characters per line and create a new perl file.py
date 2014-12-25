# encoding=utf-8
'''
Input : A Perl program file
We need to modify the file to have a max of 80 characters per line and create a new perl file.
Problem is we need to use "/" wherever we split the line and also, the split MUST happen at a place with white space. (ASSUMPTION - No is >75 characters)
'''
#分离的地方必须是white space的。。也就是word必须保留完整。而且'/'必须占用empty的位置
def split_line(content, MAX_LIMIT=5):
    ret=''
    while len(content) > MAX_LIMIT:
        words = content[:100].split(" ")
        count = 0
        index = 0
        for i in range(0, len(words)):
            count = count + len(words[i]) + 1
            if count >= MAX_LIMIT:    break
            index = index + 1

        newline = " ".join(words[:index + 1])
        content = content[len(newline):]
        if content:      ret+= newline + '/'
        else:  ret+= newline